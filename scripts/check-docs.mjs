#!/usr/bin/env node
/**
 * Lightweight integrity checks for Ops AI Library.
 * Usage: node scripts/check-docs.mjs
 */
import fs from "node:fs";
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
];

for (const f of required) {
  if (!exists(f)) fail(`missing ${f}`);
}
ok(`required files present (${required.length})`);

const data = JSON.parse(fs.readFileSync(path.join(root, "prompts/prompts.json"), "utf8"));
if (!data.prompts || data.prompts.length < 40) fail(`prompts.json too small: ${data.prompts?.length}`);
else ok(`prompts.json count=${data.prompts.length}`);

const ids = new Set(data.prompts.map((p) => p.id));
for (const id of ["P00", "P01", "P08", "P20", "P44"]) {
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

console.log("");
if (errors) {
  console.error(`FAILED with ${errors} error(s), ${warns} warning(s)`);
  process.exit(1);
}
console.log(`PASSED with ${warns} warning(s)`);
