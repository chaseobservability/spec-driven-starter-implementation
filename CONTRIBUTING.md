# Contributing (Implementation)

## Principles
- Spec-driven development: implementation must match pinned specs.
- Contracts first: OpenAPI + schemas + flows define correctness.
- Prefer vertical slices.

## Spec pinning
- Do not edit vendored spec files directly.
- To update spec:
  1) bump `spec/VERSION`
  2) vendor a new snapshot under `spec/starter-spec-v<version>/`
  3) ensure CI passes

## PR checklist
- [ ] `pnpm spec:validate` passes
- [ ] OpenAPI diff vs pinned spec is clean
- [ ] flows parse
- [ ] CI green
