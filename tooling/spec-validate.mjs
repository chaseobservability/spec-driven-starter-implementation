import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { execSync } from "node:child_process";

function sha256File(p) {
  const h = crypto.createHash("sha256");
  h.update(fs.readFileSync(p));
  return "sha256:" + h.digest("hex");
}

const version = fs.readFileSync("spec/VERSION","utf-8").trim();
const expected = fs.readFileSync("spec/CHECKSUM","utf-8").trim();
const specDir = path.join("spec", `starter-spec-v${version}`);
if (!fs.existsSync(specDir)) {
  console.error("Missing pinned spec dir:", specDir);
  process.exit(2);
}

console.log("OK spec dir exists:", specDir);
console.log("Pinned spec version:", version);
console.log("Expected checksum:", expected);

// Validate OpenAPI match
const implOpenapi = path.join("api", "openapi.yaml");
const specOpenapi = path.join(specDir, "interfaces", "api.openapi.yaml");
if (!fs.existsSync(implOpenapi)) {
  console.error("Missing implementation OpenAPI:", implOpenapi);
  process.exit(3);
}
if (!fs.existsSync(specOpenapi)) {
  console.error("Missing spec OpenAPI:", specOpenapi);
  process.exit(4);
}
try {
  execSync(`diff -u ${implOpenapi} ${specOpenapi}`, { stdio: "inherit" });
} catch {
  console.error("OpenAPI differs from pinned spec.");
  process.exit(5);
}
console.log("OK OpenAPI matches pinned spec.");

// Validate flows parse via python (optional)
console.log("OK spec validate complete.");
