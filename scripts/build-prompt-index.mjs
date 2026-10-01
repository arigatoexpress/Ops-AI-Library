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
  "late-arrival-and-service-recovery.md",
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
  "late-arrival-and-service-recovery.md": "Late arrival & service recovery",
  "00-how-to-write-prompts.md": "How to write prompts",
};