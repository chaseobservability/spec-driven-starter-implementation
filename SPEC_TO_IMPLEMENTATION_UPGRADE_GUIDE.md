# Spec → Implementation Upgrade Guide

This guide describes the safe, repeatable way to upgrade an implementation repo to a new pinned spec version.

Applies to:
- spec-driven-starter-spec
- spec-driven-starter-implementation
- and any future spec/implementation pair using this model.

---

## Goals

- Upgrade without contract drift
- Keep CI as the enforcement mechanism
- Make breaking changes explicit and versioned

---

## Pre-flight Checklist (before changing anything)

1. Read the spec release notes (`CHANGELOG.md`) for:
   - breaking changes
   - new required fields
   - workflow changes
   - schema/OpenAPI changes

2. Confirm your target versions:
   - Spec tag: `vX.Y.Z`
   - Implementation tag you’re upgrading from

3. Ensure the implementation repo is green on `main`:
   - tests pass
   - CI passes
   - no uncommitted work

---

## Upgrade Procedure (implementation repo)

### Step 1 — Pin the new spec version
Update:
- `spec/VERSION` → `X.Y.Z`

Replace vendored spec folder:
- `spec/starter-spec-vX.Y.Z/` (or equivalent naming)
- Ensure the old version remains in Git history, not necessarily in the working tree.

If you store a checksum:
- update `spec/CHECKSUM`

### Step 2 — Update implementation OpenAPI mirror
Your implementation should mirror the spec OpenAPI exactly.
Update:
- `api/openapi.yaml` ← spec `interfaces/api.openapi.yaml`

### Step 3 — Run contract enforcement locally
Run:
- `pnpm spec:validate`
- Confirm OpenAPI diff is clean

If your CI checks OpenAPI equality, make sure it passes locally first.

### Step 4 — Update code for contract changes
Common updates include:
- new required fields in schemas
- endpoint parameter changes in OpenAPI
- workflow invariant changes

Keep updates minimal and targeted:
- update domain types
- update adapters
- update handlers
- update fixtures/flow tests

### Step 5 — Update acceptance artifacts
If your implementation runs flow tests:
- update fixtures to match the new spec
- add coverage for new workflows

### Step 6 — Ship as a single cohesive change
Make one PR that includes:
- spec pin bump + vendored spec update
- OpenAPI mirror update
- code changes required for compatibility
- updated tests/fixtures

---

## Handling Breaking Spec Changes

Breaking changes must be explicit:
- spec version bumped
- migration notes written in spec release
- implementation PR references those notes

If the spec removed a field or changed a required workflow:
- prefer writing an adapter layer
- avoid rewriting core logic if possible
- preserve backward compatibility only if required operationally

---

## Post-upgrade Checklist

- CI green on implementation repo
- Ops smoke test (if applicable)
- Tag implementation release with pinned spec reference in notes

---

## Recommended Commit Message (implementation)
`chore(spec-pin): bump pinned spec to vX.Y.Z`

Followed by:
`feat: adapt to spec vX.Y.Z contracts` (if code changes needed)

---

## Recommended Release Notes (implementation)

Include:
- `Specs pinned: chaseobservability/spec-driven-starter-spec@vX.Y.Z`
- contract changes summary
- migration notes (if any)
