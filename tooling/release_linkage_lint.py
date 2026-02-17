#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHANGELOG = ROOT / "CHANGELOG.md"
VERSION_FILE = ROOT / "spec/VERSION"


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")


def ok(msg: str) -> None:
    print(f"OK: {msg}")


def main() -> int:
    version = VERSION_FILE.read_text(encoding="utf-8").strip()
    text = CHANGELOG.read_text(encoding="utf-8")

    expected = f"spec-driven-starter-spec@v{version}"
    if expected not in text:
        fail(f"CHANGELOG.md must mention pinned spec tag: {expected}")
        return 1

    ok(f"release linkage lint passed ({expected})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
