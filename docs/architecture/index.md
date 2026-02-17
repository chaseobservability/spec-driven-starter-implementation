# Architecture Index

## Contract surfaces
- Runtime OpenAPI: `api/openapi.yaml`
- Pinned upstream spec: `spec/starter-spec-v*/interfaces/api.openapi.yaml`
- Acceptance fixtures: `spec/starter-spec-v*/flows/*.yaml`

## Rules
- Keep implementation aligned to pinned spec.
- Prefer deterministic validations and fixtures.
- Treat pin/checksum drift as a CI failure.
