# Spec-Driven Starter Implementation

A **spec-driven implementation** starter template designed to be paired with:

- [spec-driven-starter-spec](https://github.com/chaseobservability/spec-driven-starter-spec)

Inspired by Sean Grove’s talk (Spec-Driven Development): [YouTube](https://youtu.be/8rABwKRsec4)

Harness engineering reference: [OpenAI Harness Engineering](https://openai.com/index/harness-engineering/)

## Get Started
```bash
git clone git@github.com:chaseobservability/spec-driven-starter-implementation.git
cd spec-driven-starter-implementation
pnpm i
```

Validate the pinned spec and implementation contract locally:

```bash
python3 tooling/harness_lint.py
python3 tooling/architecture_lint.py
python3 tooling/release_linkage_lint.py
pnpm spec:validate
python3 tooling/flow_contract_eval.py
python3 - <<'PY'
import glob, yaml
for p in glob.glob("spec/starter-spec-v*/flows/*.yaml"):
  yaml.safe_load(open(p,"r",encoding="utf-8"))
print("OK: pinned spec validation and flow parse checks")
PY
```

Execute runtime flows against a running app:

```bash
# Option A: app already running
python3 tooling/flow_runtime_eval.py --base-url http://127.0.0.1:3000

# Option B: evaluator starts app process, waits on /health, then runs flows
python3 tooling/flow_runtime_eval.py \
  --base-url http://127.0.0.1:3000 \
  --start-cmd "pnpm dev" \
  --wait-path /health \
  --wait-timeout-sec 90
```

CI always executes runtime flows using a deterministic fixture server:
- [`tooling/fixture_runtime_server.py`](tooling/fixture_runtime_server.py)
- [`tooling/flow_runtime_eval.py`](tooling/flow_runtime_eval.py)
- CI also runs a second `runtime-real` job and executes real runtime evaluation only when `package.json` defines `app:ci:start`.

Agent-first first implementation change:
1. Ask Codex to execute the change end-to-end.
2. Review behavior and compatibility in the PR.
3. Merge only after CI is green.

Suggested Codex prompt:
```text
Implement <feature/fix> in this repository while preserving pinned-spec correctness.
Do it end-to-end:
- update implementation code and api/openapi.yaml as needed
- keep alignment with spec/VERSION and spec/CHECKSUM
- run pnpm spec:validate and local checks
- if spec upgrade is required, follow SPEC_TO_IMPLEMENTATION_UPGRADE_GUIDE.md
- update CHANGELOG.md for user-visible changes
- open/push a PR and iterate until CI is green
Return the PR link and a concise compatibility summary.
```

## Spec pinning
- Spec version is pinned in [`spec/VERSION`](spec/VERSION).
- Vendored spec snapshot is in [`spec/starter-spec-v<version>/`](spec/).
- CI enforces:
  - pinned spec exists
  - OpenAPI matches spec
  - flow fixtures parse

## Key References
- Engineering guidelines: [`docs/ENGINEERING_GUIDELINES.md`](docs/ENGINEERING_GUIDELINES.md)
- Roadmap: [`ROADMAP.md`](ROADMAP.md)
- CI: [`.github/workflows/ci.yml`](.github/workflows/ci.yml)

## Scripts
- [`pnpm spec:validate`](package.json) verifies pinned spec artifacts exist
- [`pnpm harness:lint`](package.json) validates harness structure and docs links
- [`pnpm architecture:lint`](package.json) enforces starter structural guardrails
- [`pnpm release:linkage:lint`](package.json) ensures latest changelog links to pinned spec tag
- [`pnpm flow:contract:eval`](package.json) validates flow fixtures against OpenAPI declarations
- [`pnpm flow:runtime:eval`](package.json) executes flow fixtures against a running runtime
- [`pnpm fixture:runtime`](package.json) starts a deterministic runtime for flow evaluation


## Philosophy
See [`SPEC_DRIVEN_DEVELOPMENT_PHILOSOPHY.md`](SPEC_DRIVEN_DEVELOPMENT_PHILOSOPHY.md).

## Docs
- Agent map: [`AGENTS.md`](AGENTS.md)
- Harness index: [`docs/index.md`](docs/index.md)
- Starter pack contract: [`SDD_STARTER_PACK_CONTRACT.md`](SDD_STARTER_PACK_CONTRACT.md)
- Doc-gardener automation: [`.github/workflows/doc-gardener.yml`](.github/workflows/doc-gardener.yml)
- Philosophy: [`SPEC_DRIVEN_DEVELOPMENT_PHILOSOPHY.md`](SPEC_DRIVEN_DEVELOPMENT_PHILOSOPHY.md)
- Engineering guidelines: [`docs/ENGINEERING_GUIDELINES.md`](docs/ENGINEERING_GUIDELINES.md)
- ADR template: [`docs/decisions/ADR_TEMPLATE.md`](docs/decisions/ADR_TEMPLATE.md)
- Spec → Implementation upgrade guide: [`SPEC_TO_IMPLEMENTATION_UPGRADE_GUIDE.md`](SPEC_TO_IMPLEMENTATION_UPGRADE_GUIDE.md)
- Roadmap: [`ROADMAP.md`](ROADMAP.md)
- Contributing: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Release checklist: [`RELEASE_CHECKLIST.md`](RELEASE_CHECKLIST.md)
