#!/usr/bin/env node
/**
 * Rebuild prompts/prompts.json DATA and refresh explorer.html embedded DATA.
 * Usage: node scripts/build-prompt-index.mjs
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const promptsDir = path.join(root, "prompts");

const files = [
  "daily-operations.md",
  "safety-and-compliance.md",
  "meeting-and-communication.md",
  "data-and-reporting.md",
  "process-improvement.md",
  "peak-season-and-surge.md",
  "linehaul-and-routing.md",
  "governance-safe-use.md",
  "customer-and-contractor.md",
  "00-how-to-write-prompts.md",
];

const categoryNames = {
  "daily-operations.md": "Daily operations",
  "safety-and-compliance.md": "Safety & compliance",
  "meeting-and-communication.md": "Meetings & communication",
  "data-and-reporting.md": "Data & reporting",
  "process-improvement.md": "Process improvement",
  "peak-season-and-surge.md": "Peak season & surge",
  "linehaul-and-routing.md": "Linehaul & routing",
  "governance-safe-use.md": "Governance-safe use",
  "customer-and-contractor.md": "Customer & contractor",
  "00-how-to-write-prompts.md": "How to write prompts",
};

const catalogTitles = {
  "Manager template (blank)": "P00",
  "Prompt Template For Managers": "P00",
  "Daily Manager Brief": "P01",
  "Shift Handoff": "P02",
  "Escalation Summary": "P03",
  "After-Action Review": "P04",
  "Pre-Sort Stand-Up Brief": "P05",
  "End-of-Shift Closeout Checklist": "P06",
  "Volume Anomaly Quick Check": "P07",
  "Pre-Shift Safety Huddle Brief": "P08",
  "Near-Miss Report Draft": "P09",
  "Safety Meeting Agenda": "P10",
  "Seasonal Safety Alert Draft": "P11",
  "Post-Incident Team Note (Manager-to-Team)": "P12",
  "Safety Metrics Discussion Summary": "P13",
  "Meeting Agenda": "P14",
  "Meeting Notes To Action Items": "P15",
  "Professional Email Draft": "P16",
  "Executive Update": "P17",
  "Team Announcement": "P18",
  "Report Summary": "P19",
  "Metrics Interpretation": "P20",
  "Data Request Draft": "P21",
  "Dashboard Feedback": "P22",
  "“Explain This Number” For A Non-Technical Audience": "P23",
  "Explain This Number For A Non-Technical Audience": "P23",
  "Process Map From Notes": "P24",
  "Root Cause Brainstorm": "P25",
  "Pilot Design": "P26",
  "Standard Work Draft": "P27",
  "Pre-Peak Readiness Brief": "P28",
  "Surge Day Checklist": "P29",
  "Staffing Scenario Discussion (Non-Sensitive)": "P30",
  "Post-Peak After-Action": "P31",
  "Feeder / Linehaul Delay Framing": "P32",
  "Yard / Dock Coordination Notes": "P33",
  "Alternate Plan Discussion (Advisory)": "P34",
  "P&D Density / Coverage Conversation Starter": "P35",
  "Service Alert Draft (Internal First)": "P36",
  "Escalation Response Outline": "P37",
  "ISP / Contractor Briefing Draft": "P38",
  "Team Recognition Note": "P39",
  "Use Case Intake": "P40",
  "Privacy Review Preparation": "P41",
  "Accuracy Review": "P42",
  "External Sharing Check": "P43",
  "“Is This Safe To Try?”": "P44",
  "Is This Safe To Try?": "P44",
};

const agentMap = {
  P01: "Shift Brief Coach", P02: "Shift Brief Coach", P03: "Shift Brief Coach",
  P04: "Shift Brief Coach", P05: "Shift Brief Coach", P06: "Shift Brief Coach",
  P07: "Metrics Explainer",
  P08: "Safety Huddle Coach", P09: "Safety Huddle Coach", P10: "Safety Huddle Coach",
  P11: "Safety Huddle Coach", P12: "Safety Huddle Coach", P13: "Safety Huddle Coach",
  P14: "Meeting Scribe", P15: "Meeting Scribe", P16: "Meeting Scribe",
  P17: "Meeting Scribe", P18: "Meeting Scribe",
  P19: "Metrics Explainer", P20: "Metrics Explainer", P21: "Metrics Explainer",
  P22: "Metrics Explainer", P23: "Metrics Explainer",
  P24: "Process Coach", P25: "Process Coach", P26: "Process Coach", P27: "Process Coach",
  P28: "Process Coach", P29: "Shift Brief Coach", P30: "Process Coach", P31: "Process Coach",
  P32: "Shift Brief Coach", P33: "Shift Brief Coach", P34: "Process Coach", P35: "Process Coach",
  P36: "Meeting Scribe", P37: "Meeting Scribe", P38: "Meeting Scribe", P39: "Meeting Scribe",
  P40: "Governance Gatekeeper", P41: "Governance Gatekeeper", P42: "Governance Gatekeeper",
  P43: "Governance Gatekeeper", P44: "Governance Gatekeeper", P00: null,
};

const FIRST = new Set(["P01", "P02", "P08", "P15", "P20", "P44"]);
const tips = {
  P01: "Best first prompt. Scrub notes, then edit owners before sending.",
  P02: "Use at end of shift. Roles only — no personal performance notes.",
  P08: "Under 150 words. End with Safety Above All.",
  P15: "Never invent owners or due dates — use Needs assignment.",
  P20: "Hypotheses only — no causal claims without evidence.",
  P44: "Use before any new AI idea or automation request.",
};

const prompts = [];
for (const file of files) {
  const raw = fs.readFileSync(path.join(promptsDir, file), "utf8");
  const category = categoryNames[file];
  const parts = raw.split(/\n## /);
  for (let i = 1; i < parts.length; i++) {
    const part = parts[i];
    const titleLine = part.split("\n")[0].trim();
    const body = part.slice(titleLine.length).trim();
    const m = body.match(/```(?:text)?\n([\s\S]*?)```/);
    if (!m) continue;
    const text = m[1].trim();
    if (text.length < 80 && !titleLine.toLowerCase().includes("template")) continue;
    if (/^summarize this\.?$/i.test(text)) continue;
    const clean = titleLine.replace(/[“”]/g, "");
    const id = catalogTitles[titleLine] || catalogTitles[clean];
    if (!id) {
      console.warn("Skipping unmapped section:", titleLine);
      continue;
    }
    const placeholders = [...text.matchAll(/\[([^\]]+)\]/g)].map((x) => x[0]);
    prompts.push({
      id,
      title: clean,
      category,
      file,
      minutes: null,
      text,
      placeholders: [...new Set(placeholders)],
      agent: agentMap[id] || null,
      firstWeek: FIRST.has(id),
      tip: tips[id] || "Scrub sensitive data. Treat output as a draft.",
    });
  }
}

const catMd = fs.readFileSync(path.join(promptsDir, "CATALOG.md"), "utf8");
for (const row of catMd.split("\n")) {
  const m = row.match(/^\| (P\d+) \| ([^|]+) \|[^|]+\| (\d+)/);
  if (!m) continue;
  const p = prompts.find((x) => x.id === m[1]);
  if (p) p.minutes = Number(m[3]);
}

prompts.sort((a, b) => Number(a.id.replace(/\D/g, "")) - Number(b.id.replace(/\D/g, "")));

const data = {
  generated: new Date().toISOString().slice(0, 10),
  version: "1.3",
  count: prompts.length,
  rule: "AI drafts. You decide. Never paste tracking numbers, customer names, employee records, routes, or credentials into unapproved tools.",
  prompts,
};

fs.writeFileSync(path.join(promptsDir, "prompts.json"), JSON.stringify(data, null, 2) + "\n");

const explorerPath = path.join(promptsDir, "explorer.html");
if (fs.existsSync(explorerPath)) {
  let html = fs.readFileSync(explorerPath, "utf8");
  const re = /const DATA = [\s\S]*?;\nconst FIRST_WEEK/;
  if (!re.test(html)) {
    console.warn("explorer.html DATA block not found for replacement; JSON updated only.");
  } else {
    html = html.replace(re, `const DATA = ${JSON.stringify(data)};\nconst FIRST_WEEK`);
    fs.writeFileSync(explorerPath, html);
    console.log("Updated explorer.html DATA");
  }
}

console.log(`Built prompts.json (${data.count} prompts)`);
