#!/usr/bin/env python3
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = [
    ("bodyobservability/spec-driven-starter-spec", "chaseobservability/spec-driven-starter-spec"),
    ("bodyobservability/spec-driven-starter-implementation", "chaseobservability/spec-driven-starter-implementation"),
    ("## Quickstart", "## Get Started"),
    ("## Where to start", "## Key References"),
]

SKIP_PREFIXES = [".git/", "spec/starter-spec-v"]


def iter_markdown_files():
    for p in ROOT.rglob("*.md"):
        rel = p.relative_to(ROOT).as_posix()
        if any(rel.startswith(prefix) for prefix in SKIP_PREFIXES):
            continue
        yield p


def normalize_text(text: str) -> str:
    out = text
    for old, new in REPLACEMENTS:
        out = out.replace(old, new)
    out = re.sub(r"[ \t]+$", "", out, flags=re.MULTILINE)
    if not out.endswith("\n"):
        out += "\n"
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Auto-fix low-risk documentation drift.")
    parser.add_argument("--check", action="store_true", help="Only check; exit non-zero if changes needed")
    args = parser.parse_args()

    changed = []
    for p in iter_markdown_files():
        src = p.read_text(encoding="utf-8")
        dst = normalize_text(src)
        if dst != src:
            changed.append(p)
            if not args.check:
                p.write_text(dst, encoding="utf-8")

    if changed:
        print("doc-gardener changes needed:")
        for p in changed:
            print(f"- {p.relative_to(ROOT)}")
        return 1 if args.check else 0

    print("doc-gardener: no changes needed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
