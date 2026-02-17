#!/usr/bin/env python3
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "AGENTS.md",
    "SDD_STARTER_PACK_CONTRACT.md",
    "README.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "RELEASE_CHECKLIST.md",
    "ROADMAP.md",
    "docs/index.md",
    "docs/architecture/index.md",
    "docs/product-specs/index.md",
    "docs/references/index.md",
    "docs/exec-plans/tech-debt-tracker.md",
    "spec/VERSION",
    "spec/CHECKSUM",
    "tooling/spec-validate.mjs",
    "tooling/flow_runtime_eval.py",
    "tooling/fixture_runtime_server.py",
    "tooling/architecture_lint.py",
    "tooling/release_linkage_lint.py",
]

REQUIRED_DIRS = [
    "docs/exec-plans/active",
    "docs/exec-plans/completed",
    "spec",
    "api",
    "tooling",
]

MAX_AGENTS_LINES = 180


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")


def ok(msg: str) -> None:
    print(f"OK: {msg}")


def check_paths() -> list[str]:
    errs = []
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            errs.append(f"missing file: {rel}")
    for rel in REQUIRED_DIRS:
        if not (ROOT / rel).is_dir():
            errs.append(f"missing directory: {rel}")
    return errs


def check_agents_size() -> list[str]:
    p = ROOT / "AGENTS.md"
    if not p.exists():
        return ["AGENTS.md missing"]
    lines = p.read_text(encoding="utf-8").splitlines()
    if len(lines) > MAX_AGENTS_LINES:
        return [f"AGENTS.md too long ({len(lines)} lines > {MAX_AGENTS_LINES})"]
    return []


def check_index_links() -> list[str]:
    p = ROOT / "docs/index.md"
    if not p.exists():
        return ["docs/index.md missing"]
    errs = []
    text = p.read_text(encoding="utf-8")
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
    for link in links:
        if link.startswith("http://") or link.startswith("https://") or link.startswith("#"):
            continue
        target = (p.parent / link).resolve() if not link.startswith("/") else (ROOT / link[1:]).resolve()
        if ROOT.resolve() not in target.parents and target != ROOT.resolve():
            errs.append(f"docs/index.md has out-of-repo link: {link}")
            continue
        if not target.exists():
            errs.append(f"docs/index.md points to missing path: {link}")
    return errs


def main() -> int:
    errs = []
    errs.extend(check_paths())
    errs.extend(check_agents_size())
    errs.extend(check_index_links())

    if errs:
        for e in errs:
            fail(e)
        return 1

    ok("harness lint passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
