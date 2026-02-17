# Product Specs Index

Product behavior is implemented against pinned upstream contracts.

## Primary artifacts
- Implementation API contract: `api/openapi.yaml`
- Pinned spec metadata: `spec/VERSION`, `spec/CHECKSUM`
- Vendored acceptance scenarios: `spec/starter-spec-v*/flows/*.yaml`

## Change process
- Update implementation contract intentionally.
- Re-pin spec snapshot when upstream contracts change.
- Run `pnpm spec:validate` before merge.
