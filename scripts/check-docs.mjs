#!/usr/bin/env node
/**
 * Lightweight integrity checks for Ops AI Library.
 * Usage: node scripts/check-docs.mjs
 */
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
let errors = 0;
let warns = 0;

function fail(msg) {
  console.error("ERROR:", msg);
  errors++;
}
function warn(msg) {
  console.warn("WARN:", msg);
  warns++;
}
function ok(msg) {
  console.log("OK:", msg);
}

function exists(rel) {
  return fs.existsSync(path.join(root, rel));
}

const required = [
  "README.md",
  "index.html",
  "prompts/explorer.html",
  "prompts/prompts.json",
  "prompts/CATALOG.md",
  "docs/meeting-one-pager.md",
  "docs/manager-wallet-card.md",
  "docs/print-pack-first-week.md",
  "docs/faq.md",
  "governance/safe-use-rules.md",
  "governance/data-cards.md",
  "souls/shift-brief-coach.md",
  "playbooks/sharepoint-power-automate.md",
  "playbooks/power-automate-flow-specs.md",
  "playbooks/gcp-sandbox.md",
  "demos/01-shift-brief.md",
  "starter-kits/wrong-day-lates/README.md",
];

for (const f of required) {
  if (!exists(f)) fail(`missing ${f}`);
}
ok(`required files present (${required.length})`);

const data = JSON.parse(fs.readFileSync(path.join(root, "prompts/prompts.json"), "utf8"));
if (!data.prompts || data.prompts.length < 40) fail(`prompts.json too small: ${data.prompts?.length}`);
else ok(`prompts.json count=${data.prompts.length}`);

const ids = new Set(data.prompts.map((p) => p.id));
for (const id of ["P00", "P01", "P08", "P20", "P44", "P45", "P46", "P47", "P48"]) {
  if (!ids.has(id)) fail(`missing prompt id ${id}`);
}

const catalog = fs.readFileSync(path.join(root, "prompts/CATALOG.md"), "utf8");
const catIds = [...catalog.matchAll(/\| (P\d+) \|/g)].map((m) => m[1]);
for (const id of catIds) {
  if (!ids.has(id) && id !== "P00") {
    // P00 may be template-only in json as Manager template
  }
  if (!ids.has(id)) warn(`catalog id not in prompts.json: ${id}`);
}
ok(`catalog rows=${catIds.length}`);

const explorer = fs.readFileSync(path.join(root, "prompts/explorer.html"), "utf8");
if (!explorer.includes("const DATA =")) fail("explorer missing DATA");
if (!explorer.includes("Daily Manager Brief")) fail("explorer missing Daily Manager Brief");
if (!explorer.includes("scanSensitive") && !explorer.includes("Sensitivity scan"))
  warn("explorer may be missing sensitivity scan (older build?)");
else ok("explorer has sensitivity features or legacy copy");

// relative markdown links in README
const readme = fs.readFileSync(path.join(root, "README.md"), "utf8");
const linkRe = /\]\((?!https?:|mailto:|#)([^)]+)\)/g;
let m;
while ((m = linkRe.exec(readme))) {
  let target = m[1].split("#")[0].split("?")[0];
  if (!target) continue;
  target = decodeURIComponent(target);
  if (!exists(target)) fail(`README broken link: ${target}`);
}
ok("README relative links resolve");

if (!readme.includes("explorer.html")) warn("README should feature explorer.html");
if (!readme.includes("AI drafts")) warn("README missing core rule phrase");

// Secret-filename scan: flag secrets.toml, .pem, .key, .env, credential files.
// Success line prints only when this walk finds nothing; failure still records an error and exits non-zero.
//
// Owner decision: the travis-vscode-repo/ contributor tree stays. Skip that
// path prefix only — it previously held a 0-byte .streamlit/secrets.toml, and
// deleting the folder is not the fix. Do not broaden this list. Every other
// path is still scanned.
const SECRET_SCAN_EXCLUDE_PREFIXES = ["travis-vscode-repo/"];
const secretRe = /(^|\/)(secrets\.toml|\.env|.*\.pem|.*\.key|credentials?\.(json|yml|yaml|txt)|id_rsa.*)$/i;

function toPosix(p) {
  return p.split(path.sep).join("/");
}

function isUnderExcludedPrefix(relPosix, prefixes) {
  return prefixes.some((prefix) => {
    const dir = prefix.endsWith("/") ? prefix.slice(0, -1) : prefix;
    return relPosix === dir || relPosix.startsWith(`${dir}/`);
  });
}

function scanSecretFilenames(scanRoot, excludePrefixes) {
  const hits = [];
  function walk(dir) {
    for (const ent of fs.readdirSync(dir, { withFileTypes: true })) {
      const abs = path.join(dir, ent.name);
      const rel = toPosix(path.relative(scanRoot, abs));
      if (isUnderExcludedPrefix(rel, excludePrefixes)) continue;
      if (ent.isDirectory()) {
        if (ent.name === ".git" || ent.name === "node_modules") continue;
        walk(abs);
      } else if (secretRe.test(rel)) {
        hits.push(rel);
      }
    }
  }
  walk(scanRoot);
  return hits;
}

// Self-test writes a temp tree outside the repo and deletes it before exit.
// It must flag a secret-like name elsewhere, including a near-miss folder
// name, and it must ignore the same name under travis-vscode-repo/.
function runSecretScanSelfTest() {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "ops-ai-secret-scan-"));
  const flagged = "elsewhere/secrets.toml";
  const excluded = "travis-vscode-repo/.streamlit/secrets.toml";
  const nearMiss = "travis-vscode-repo-extra/secrets.toml";
  const before = errors;
  try {
    for (const rel of [flagged, excluded, nearMiss]) {
      const abs = path.join(tmp, ...rel.split("/"));
      fs.mkdirSync(path.dirname(abs), { recursive: true });
      fs.writeFileSync(abs, "");
    }
    fs.writeFileSync(path.join(tmp, "notes.txt"), "not a secret filename");
    const hits = new Set(scanSecretFilenames(tmp, SECRET_SCAN_EXCLUDE_PREFIXES));
    if (!hits.has(flagged)) fail(`self-test: expected secret-like filename to be flagged: ${flagged}`);
    if (!hits.has(nearMiss)) fail(`self-test: prefix exclusion is too broad, missed ${nearMiss}`);
    if (hits.has(excluded) || [...hits].some((h) => h === "travis-vscode-repo" || h.startsWith("travis-vscode-repo/"))) {
      fail(`self-test: ${excluded} should be excluded by prefix travis-vscode-repo/`);
    }
    if (hits.has("notes.txt")) fail("self-test: notes.txt should not be flagged");
    if (errors === before) {
      ok("secret-filename self-test: flags secrets.toml outside travis-vscode-repo/ and skips that prefix");
    }
  } finally {
    fs.rmSync(tmp, { recursive: true, force: true });
  }
}

runSecretScanSelfTest();

const repoHits = scanSecretFilenames(root, SECRET_SCAN_EXCLUDE_PREFIXES);
for (const hit of repoHits) fail(`secret-like filename in repo: ${hit}`);
if (repoHits.length === 0) ok("no secret-like filenames in tree");

console.log("");
if (errors) {
  console.error(`FAILED with ${errors} error(s), ${warns} warning(s)`);
  process.exit(1);
}
console.log(`PASSED with ${warns} warning(s)`);
