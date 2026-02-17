# AGENTS.md

This repository is agent-first. Keep this file short and use it as a map.

## Mission
- Deliver implementation that conforms to pinned spec artifacts.
- Keep validation deterministic and CI-enforced.

## Start Here
- Repo overview: `README.md`
- Engineering guardrails: `docs/ENGINEERING_GUIDELINES.md`
- Harness map: `docs/index.md`
- Architecture map: `docs/architecture/index.md`
- Product/spec map: `docs/product-specs/index.md`
- Execution plans: `docs/exec-plans/`
- References: `docs/references/index.md`

## Source of Truth
- Runtime contract: `api/openapi.yaml`
- Pinned spec version: `spec/VERSION`
- Pinned checksum: `spec/CHECKSUM`
- Spec validation: `tooling/spec-validate.mjs`

## Invariants
- `pnpm spec:validate` must pass.
- OpenAPI must match pinned spec snapshot.
- Vendored flow fixtures must parse.

## Workflow
1. Plan the change (docs/exec-plans for non-trivial scope).
2. Implement in small slices.
3. Validate with local checks and CI.
4. Keep docs and decisions in-repo.

## CI Expectations
- Install succeeds.
- Pinned spec/openapi validation succeeds.
- Vendored flows parse.
- Governance + harness docs exist.
