# SDD Starter Pack Contract

This repository is one half of the starter pack.

## Compatibility handshake
- Spec repo publishes tagged versions `vX.Y.Z`.
- Implementation repo pins one exact spec version and checksum.
- Upgrade flow follows `SPEC_TO_IMPLEMENTATION_UPGRADE_GUIDE.md`.

## Release order
1. Update and tag spec contracts.
2. Vendor/pin updated spec in implementation.
3. Run CI in both repos.
4. Publish release notes with compatibility statement.

## Compatibility statement format
- `Specs pinned: chaseobservability/spec-driven-starter-spec@vX.Y.Z`
