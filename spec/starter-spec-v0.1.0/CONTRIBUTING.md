# Contributing (Specs)

## Principles
- Specs are upstream contracts. Implementation follows.
- Prefer deterministic, explainable rules.
- Acceptance fixtures are part of the contract.

## Breaking vs non-breaking
Breaking changes include:
- OpenAPI shape changes
- schema changes that remove/rename required fields
- invariant changes
- packet/export contract changes

Breaking changes require:
- version bump
- changelog entry
- updated acceptance artifacts

## PR checklist
- [ ] CHANGELOG updated
- [ ] OpenAPI parses
- [ ] Schemas parse
- [ ] Flows parse
- [ ] CI green
