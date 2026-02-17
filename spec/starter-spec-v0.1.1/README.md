# Spec-Driven Starter Spec

A **contract-first spec** starter template designed to be paired with:

- [spec-driven-starter-implementation](https://github.com/chaseobservability/spec-driven-starter-implementation)

Inspired by Sean Grove’s talk (Spec-Driven Development): [YouTube](https://youtu.be/8rABwKRsec4)

Harness engineering reference: [OpenAI Harness Engineering](https://openai.com/index/harness-engineering/)

## Quickstart
```bash
git clone git@github.com:chaseobservability/spec-driven-starter-spec.git
cd spec-driven-starter-spec
```

Validate the starter contracts locally:

```bash
python3 - <<'PY'
import yaml, json, glob
yaml.safe_load(open("interfaces/api.openapi.yaml","r",encoding="utf-8"))
for p in glob.glob("schemas/*.json"):
  json.load(open(p,"r",encoding="utf-8"))
for p in glob.glob("flows/*.yaml"):
  yaml.safe_load(open(p,"r",encoding="utf-8"))
print("OK: OpenAPI, schemas, and flows parse")
PY
```

Make your first spec change:
1. Update OpenAPI in [`interfaces/api.openapi.yaml`](interfaces/api.openapi.yaml).
2. Add or update related schemas in [`schemas/`](schemas/).
3. Add or update acceptance fixtures in [`flows/`](flows/).
4. Update [`CHANGELOG.md`](CHANGELOG.md) for user-visible changes.
5. Open a PR and ensure CI is green.

## What belongs here
- API contract (OpenAPI)
- Data contracts (JSON Schemas)
- Deterministic rules and invariants
- Executable workflow specs (flow fixtures)
- Acceptance criteria
- Release and governance docs

## Starter examples
- Todo API paths in OpenAPI:
  - [`interfaces/api.openapi.yaml`](interfaces/api.openapi.yaml) (`POST /todos`, `GET /todos`, `GET /todos/{id}`)
- Todo schemas:
  - [`schemas/todo-create-request.schema.json`](schemas/todo-create-request.schema.json)
  - [`schemas/todo-item.schema.json`](schemas/todo-item.schema.json)
- Todo acceptance flows:
  - [`flows/create_todo_happy_path.yaml`](flows/create_todo_happy_path.yaml)
  - [`flows/create_todo_validation_error.yaml`](flows/create_todo_validation_error.yaml)

## Where to start
- API contract: [`interfaces/api.openapi.yaml`](interfaces/api.openapi.yaml)
- Schemas: [`schemas/`](schemas/)
- Flows: [`flows/`](flows/)
- Engineering guidelines: [`docs/ENGINEERING_GUIDELINES.md`](docs/ENGINEERING_GUIDELINES.md)
- Roadmap: [`ROADMAP.md`](ROADMAP.md)

## Versioning
- Tag releases as `vX.Y.Z`.
- Breaking contract changes require a version bump and updated acceptance artifacts.

See [`RELEASE_CHECKLIST.md`](RELEASE_CHECKLIST.md).


## Philosophy
See [`SPEC_DRIVEN_DEVELOPMENT_PHILOSOPHY.md`](SPEC_DRIVEN_DEVELOPMENT_PHILOSOPHY.md).

## Docs
- Agent map: [`AGENTS.md`](AGENTS.md)
- Harness index: [`docs/index.md`](docs/index.md)
- Starter pack contract: [`SDD_STARTER_PACK_CONTRACT.md`](SDD_STARTER_PACK_CONTRACT.md)
- Philosophy: [`SPEC_DRIVEN_DEVELOPMENT_PHILOSOPHY.md`](SPEC_DRIVEN_DEVELOPMENT_PHILOSOPHY.md)
- Engineering guidelines: [`docs/ENGINEERING_GUIDELINES.md`](docs/ENGINEERING_GUIDELINES.md)
- ADR template: [`docs/decisions/ADR_TEMPLATE.md`](docs/decisions/ADR_TEMPLATE.md)
- Spec → Implementation upgrade guide: [`SPEC_TO_IMPLEMENTATION_UPGRADE_GUIDE.md`](SPEC_TO_IMPLEMENTATION_UPGRADE_GUIDE.md)
- Roadmap: [`ROADMAP.md`](ROADMAP.md)
- Contributing: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Release checklist: [`RELEASE_CHECKLIST.md`](RELEASE_CHECKLIST.md)
