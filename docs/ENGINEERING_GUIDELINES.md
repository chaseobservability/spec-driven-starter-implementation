# Engineering Guidelines (Implementation)

## Golden rules
1) Specs are upstream. Implementation pins exact spec version.
2) No contract drift: impl OpenAPI must match spec OpenAPI.
3) Add tests for behavior changes (contract/flow tests).
4) Keep business logic separate from transport and persistence.

## CI expectations
CI must fail if:
- spec artifacts are missing
- OpenAPI differs from pinned spec
- flows cannot be parsed
