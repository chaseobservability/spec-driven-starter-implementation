# Engineering Guidelines (Specs)

## Golden rules
1) This repo owns the contracts.
2) Contracts are enforceable artifacts, not prose.
3) Every contract change must come with acceptance updates.
4) Prefer deterministic rules over ambiguous language.

## Required artifacts
- OpenAPI contract: `interfaces/api.openapi.yaml`
- JSON Schemas: `schemas/*.schema.json`
- Executable flows: `flows/*.yaml`

## CI expectations
CI must fail if:
- OpenAPI cannot be parsed
- JSON schema cannot be parsed
- flows cannot be parsed
