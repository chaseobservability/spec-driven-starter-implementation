#!/usr/bin/env python3
import glob
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]

ACTION_MAP = {
    "health_check": ("/health", "get"),
    "create_todo": ("/todos", "post"),
    "get_todo": ("/todos/{id}", "get"),
}


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")


def ok(msg: str) -> None:
    print(f"OK: {msg}")


def load_yaml(p: Path):
    return yaml.safe_load(p.read_text(encoding="utf-8"))


def main() -> int:
    version = (ROOT / "spec/VERSION").read_text(encoding="utf-8").strip()
    openapi_path = ROOT / "api/openapi.yaml"
    flow_glob = str(ROOT / f"spec/starter-spec-v{version}/flows/*.yaml")

    spec = load_yaml(openapi_path)
    paths = spec.get("paths", {})

    errors: list[str] = []
    flow_files = sorted(glob.glob(flow_glob))
    if not flow_files:
        errors.append(f"no flow files found for pinned version {version}")

    for flow_file in flow_files:
        flow_path = Path(flow_file)
        flow = load_yaml(flow_path)
        steps = flow.get("steps", [])
        for i, step in enumerate(steps, start=1):
            action = step.get("action")
            status = step.get("expect_status")
            if action not in ACTION_MAP:
                errors.append(f"{flow_path.name}:step#{i} unknown action '{action}' (add to ACTION_MAP)")
                continue
            api_path, method = ACTION_MAP[action]
            op = paths.get(api_path, {}).get(method)
            if op is None:
                errors.append(f"{flow_path.name}:step#{i} missing operation {method.upper()} {api_path} in api/openapi.yaml")
                continue
            if status is not None:
                code = str(status)
                responses = op.get("responses", {})
                if code not in responses:
                    errors.append(
                        f"{flow_path.name}:step#{i} expects status {code} but {method.upper()} {api_path} does not declare it"
                    )

    if errors:
        for e in errors:
            fail(e)
        return 1

    ok(f"flow contract eval passed for spec v{version} ({len(flow_files)} flow files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
