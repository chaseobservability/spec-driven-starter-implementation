#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Minimal structural guardrails for starter implementation harness.
REQUIRED_TOP_LEVEL = {
    "api",
    "spec",
    "tooling",
    "docs",
}

FORBIDDEN_TOP_LEVEL = {
    "tmp",
    "scratch",
    "notes",
}


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")


def ok(msg: str) -> None:
    print(f"OK: {msg}")


def main() -> int:
    errors = []

    top_level = {p.name for p in ROOT.iterdir() if p.is_dir()}
    missing = sorted(REQUIRED_TOP_LEVEL - top_level)
    for name in missing:
        errors.append(f"missing required top-level directory: {name}")

    bad = sorted(FORBIDDEN_TOP_LEVEL & top_level)
    for name in bad:
        errors.append(f"forbidden top-level directory present: {name}")

    # Keep tooling scripts reasonably small and legible for agents.
    for p in (ROOT / "tooling").glob("*.py"):
        line_count = len(p.read_text(encoding="utf-8").splitlines())
        if line_count > 500:
            errors.append(f"tooling script too large (>500 lines): {p.relative_to(ROOT)} ({line_count})")

    if errors:
        for e in errors:
            fail(e)
        return 1

    ok("architecture lint passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
