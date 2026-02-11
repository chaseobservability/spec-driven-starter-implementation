# Starter Spec Repo (Sean-Grove Style)

This repository is a **contract-first spec** starter template.

It is intended to be paired with the implementation starter:
- https://github.com/<ORG>/sean-grove-starter-implementation

## What belongs here
- API contract (OpenAPI)
- Data contracts (JSON Schemas)
- Deterministic rules and invariants
- Executable workflow specs (flow fixtures)
- Acceptance criteria
- Release and governance docs

## Where to start
- API contract: `interfaces/api.openapi.yaml`
- Schemas: `schemas/`
- Flows: `flows/`
- Engineering guidelines: `docs/ENGINEERING_GUIDELINES.md`
- Roadmap: `ROADMAP.md`

## Versioning
- Tag releases as `vX.Y.Z`.
- Breaking contract changes require a version bump and updated acceptance artifacts.

See `RELEASE_CHECKLIST.md`.
