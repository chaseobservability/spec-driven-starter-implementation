# Spec-Driven Starter Implementation

A **spec-driven implementation** starter template designed to be paired with:

- https://github.com/bodyobservability/spec-driven-starter-spec

Inspired by Sean Grove’s talk (Spec-Driven Development): https://youtu.be/8rABwKRsec4

## Spec pinning
- Spec version is pinned in `spec/VERSION`.
- Vendored spec snapshot is in `spec/starter-spec-v<version>/`.
- CI enforces:
  - pinned spec exists
  - OpenAPI matches spec
  - flow fixtures parse

## Where to start
- Engineering guidelines: `docs/ENGINEERING_GUIDELINES.md`
- Roadmap: `ROADMAP.md`
- CI: `.github/workflows/ci.yml`

## Scripts
- `pnpm spec:validate` verifies pinned spec artifacts exist


## Philosophy
See `SPEC_DRIVEN_DEVELOPMENT_PHILOSOPHY.md`.

## Docs
- Philosophy: `SPEC_DRIVEN_DEVELOPMENT_PHILOSOPHY.md`
- Engineering guidelines: `docs/ENGINEERING_GUIDELINES.md`
- ADR template: `docs/decisions/ADR_TEMPLATE.md`
- Spec → Implementation upgrade guide: `SPEC_TO_IMPLEMENTATION_UPGRADE_GUIDE.md`
- Roadmap: `ROADMAP.md`
- Contributing: `CONTRIBUTING.md`
- Release checklist: `RELEASE_CHECKLIST.md`
