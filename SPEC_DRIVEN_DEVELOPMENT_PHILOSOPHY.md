# Spec‑Driven Development Philosophy

Spec‑Driven Development treats specifications as executable contracts, not documentation.

Inspired by Sean Grove’s Spec‑Driven Development principles:
https://youtu.be/8rABwKRsec4

---

## Core Principle

**Specs are upstream. Implementation is downstream.**

The specification repository defines the contracts:
- API surface (OpenAPI)
- Data contracts (JSON Schemas)
- Deterministic rules and invariants
- Workflow expectations (flow fixtures)
- Acceptance criteria

The implementation repository pins an exact spec version and must conform to it.

---

## Why This Matters

Traditional development often allows drift:
- Docs diverge from behavior
- APIs change without coordination
- Acceptance criteria live in tickets, not code

Spec‑Driven Development prevents drift by making contracts machine‑verifiable.

If it’s not in the spec, it’s not part of the system.

---

## Contracts, Not Comments

A proper spec includes:

- **OpenAPI contract** (interfaces are explicit)
- **JSON Schemas** (data shape is enforceable)
- **Executable flows** (workflows are testable)
- **Packet/export contracts** (artifacts are reproducible)
- **Acceptance fixtures** (expected behavior is encoded)

These are not optional documentation — they are the definition of correctness.

---

## Determinism Over Ambiguity

Rules must be:

- Deterministic
- Explainable
- Versioned

“Business logic” should never be hidden in controllers or UI layers.
It belongs in the contract layer (spec) or core domain layer (implementation).

---

## Versioning Discipline

Breaking contract changes require:

1. Version bump
2. Changelog entry
3. Updated acceptance fixtures
4. Coordination with downstream implementation

Implementation repos must:

- Pin spec version
- Fail CI if OpenAPI drifts
- Fail CI if flow fixtures break

---

## Vertical Slices

Build complete, small end‑to‑end behavior:

Spec → Implementation → Acceptance → Release

Do not build infrastructure in isolation from a real contract.

---

## Compliance & Audit

Spec‑Driven Development is especially powerful in regulated domains:

- Every action is auditable
- Every artifact is reproducible
- Every export has a manifest
- Every workflow is testable

This reduces operational and regulatory risk.

---

## The Discipline

Spec‑Driven Development requires:

- Saying “no” to undocumented behavior
- Versioning intentionally
- Treating acceptance tests as part of the contract
- Keeping implementation honest via CI

---

## Summary

Specs define truth.
Implementation proves compliance.
CI enforces alignment.
Versioning preserves integrity.

That is Spec‑Driven Development.
