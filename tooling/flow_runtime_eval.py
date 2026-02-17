#!/usr/bin/env python3
import argparse
import glob
import json
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Optional

import yaml

ROOT = Path(__file__).resolve().parents[1]

ACTION_MAP = {
    "health_check": ("GET", "/health"),
    "create_todo": ("POST", "/todos"),
    "get_todo": ("GET", "/todos/{id}"),
}


def log(msg: str) -> None:
    print(msg)


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")


def load_yaml(p: Path):
    return yaml.safe_load(p.read_text(encoding="utf-8"))


def normalize_base_url(base_url: str) -> str:
    return base_url.rstrip("/")


def http_request(method: str, url: str, body: Optional[dict] = None, timeout: float = 10.0):
    data = None
    headers = {"Accept": "application/json"}
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url=url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8") if resp.readable() else ""
            # reopening read is not possible; raw from first read call only
            # we already consumed once above
            body_text = raw
            status = resp.status
    except urllib.error.HTTPError as e:
        body_text = e.read().decode("utf-8") if e.fp else ""
        status = e.code
    parsed = None
    if body_text:
        try:
            parsed = json.loads(body_text)
        except json.JSONDecodeError:
            parsed = body_text
    return status, parsed


def wait_until_ready(base_url: str, wait_path: str, timeout_sec: int) -> None:
    deadline = time.time() + timeout_sec
    url = f"{base_url}{wait_path}"
    while time.time() < deadline:
        try:
            status, _ = http_request("GET", url, None, timeout=2.0)
            if 200 <= status < 500:
                log(f"OK: runtime ready at {url} (status {status})")
                return
        except Exception:
            pass
        time.sleep(1)
    raise RuntimeError(f"runtime did not become ready within {timeout_sec}s: {url}")


def assert_expectations(flow_name: str, step_index: int, expect: dict, resp_body, context: dict):
    prefix = f"{flow_name}:step#{step_index}"
    if not expect:
        return

    if "has_fields" in expect:
        if not isinstance(resp_body, dict):
            raise AssertionError(f"{prefix} expected JSON object body for has_fields")
        for field in expect["has_fields"]:
            if field not in resp_body:
                raise AssertionError(f"{prefix} missing expected field '{field}'")

    if "equals" in expect:
        if not isinstance(resp_body, dict):
            raise AssertionError(f"{prefix} expected JSON object body for equals")
        for k, v in expect["equals"].items():
            if resp_body.get(k) != v:
                raise AssertionError(f"{prefix} expected body[{k!r}] == {v!r}, got {resp_body.get(k)!r}")

    if "contains" in expect:
        contains = expect["contains"]
        if isinstance(resp_body, dict):
            for k, v in contains.items():
                actual = resp_body.get(k)
                if v not in str(actual):
                    raise AssertionError(f"{prefix} expected body[{k!r}] to contain {v!r}, got {actual!r}")
        else:
            raw = str(resp_body)
            for _, v in contains.items():
                if v not in raw:
                    raise AssertionError(f"{prefix} expected response body to contain {v!r}")

    # Persist common IDs for later steps.
    if isinstance(resp_body, dict) and "id" in resp_body:
        context["id"] = resp_body["id"]


def build_path(template: str, step: dict, context: dict) -> str:
    path = template
    params = step.get("params", {})
    if "{id}" in path:
        if "id_from_previous" in params:
            key = params["id_from_previous"]
            if key not in context:
                raise KeyError(f"missing '{key}' in flow context for path substitution")
            path = path.replace("{id}", urllib.parse.quote(str(context[key]), safe=""))
        elif "id" in params:
            path = path.replace("{id}", urllib.parse.quote(str(params["id"]), safe=""))
        else:
            raise KeyError("path requires id param, but none provided")
    return path


def run_flows(base_url: str, version: str) -> int:
    flow_files = sorted(glob.glob(str(ROOT / f"spec/starter-spec-v{version}/flows/*.yaml")))
    if not flow_files:
        fail(f"no flow files found for pinned version {version}")
        return 1

    errors = []
    for flow_file in flow_files:
        flow_path = Path(flow_file)
        flow = load_yaml(flow_path)
        flow_name = flow.get("name", flow_path.stem)
        steps = flow.get("steps", [])
        context = {}

        log(f"RUN: {flow_name} ({flow_path.name})")
        for i, step in enumerate(steps, start=1):
            action = step.get("action")
            if action not in ACTION_MAP:
                errors.append(f"{flow_name}:step#{i} unknown action '{action}'")
                continue

            method, path_template = ACTION_MAP[action]
            try:
                path = build_path(path_template, step, context)
            except Exception as e:
                errors.append(f"{flow_name}:step#{i} path build error: {e}")
                continue

            url = f"{base_url}{path}"
            req_body = step.get("request")
            expected_status = step.get("expect_status")

            try:
                status, resp_body = http_request(method, url, req_body)
                log(f"  STEP {i}: {method} {path} -> {status}")
                if expected_status is not None and status != int(expected_status):
                    errors.append(
                        f"{flow_name}:step#{i} expected status {expected_status}, got {status} for {method} {path}"
                    )
                    continue
                assert_expectations(flow_name, i, step.get("expect_body", {}), resp_body, context)
            except Exception as e:
                errors.append(f"{flow_name}:step#{i} runtime error: {e}")

    if errors:
        for e in errors:
            fail(e)
        return 1

    log(f"OK: runtime flow evaluation passed ({len(flow_files)} flow files)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Execute pinned flow fixtures against a running runtime.")
    parser.add_argument("--base-url", default="http://127.0.0.1:3000", help="Base URL for runtime under test")
    parser.add_argument("--start-cmd", default="", help="Optional command to start runtime before evaluation")
    parser.add_argument("--wait-path", default="/health", help="Path checked for readiness")
    parser.add_argument("--wait-timeout-sec", type=int, default=60, help="Readiness wait timeout")
    args = parser.parse_args()

    version = (ROOT / "spec/VERSION").read_text(encoding="utf-8").strip()
    base_url = normalize_base_url(args.base_url)

    proc = None
    try:
        if args.start_cmd:
            log(f"RUN: starting runtime with command: {args.start_cmd}")
            proc = subprocess.Popen(args.start_cmd, shell=True, cwd=ROOT)
            wait_until_ready(base_url, args.wait_path, args.wait_timeout_sec)
        return run_flows(base_url, version)
    finally:
        if proc is not None:
            proc.terminate()
            try:
                proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                proc.kill()


if __name__ == "__main__":
    sys.exit(main())
