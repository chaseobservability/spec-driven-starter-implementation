# Spec-Driven Starter Implementation

A **spec-driven implementation** starter template designed to be paired with:

- [spec-driven-starter-spec](https://github.com/chaseobservability/spec-driven-starter-spec)

Inspired by Sean Grove’s talk (Spec-Driven Development): [YouTube](https://youtu.be/8rABwKRsec4)

Harness engineering reference: [OpenAI Harness Engineering](https://openai.com/index/harness-engineering/)

## Spec pinning
- Spec version is pinned in [`spec/VERSION`](spec/VERSION).
- Vendored spec snapshot is in [`spec/starter-spec-v<version>/`](spec/).
- CI enforces:
  - pinned spec exists
  - OpenAPI matches spec
  - flow fixtures parse

## Where to start
- Engineering guidelines: [`docs/ENGINEERING_GUIDELINES.md`](docs/ENGINEERING_GUIDELINES.md)
- Roadmap: [`ROADMAP.md`](ROADMAP.md)
- CI: [`.github/workflows/ci.yml`](.github/workflows/ci.yml)

## Scripts
- [`pnpm spec:validate`](package.json) verifies pinned spec artifacts exist


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
