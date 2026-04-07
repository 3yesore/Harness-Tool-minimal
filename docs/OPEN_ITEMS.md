# Open Items

This document records the intentionally unfinished parts of the current base.

## Kept open on purpose
- Adapter layer is protocol-first, not a full runtime yet
- OS / multi-agent / external project integration remains bridge-scoped
- Adapter validation matrix remains minimal
- Adapter pack/versioning rules remain to be hardened only when needed

## Why this stays open
- To preserve extension space
- To avoid premature platformization
- To keep the core thin while the boundary hardens

## How to use this document
- Treat it as the handoff note for the next upgrade round
- Do not move these items into `core` unless they become contract-level requirements
- Expand the adapter layer only after a sample proves the need

## OpenHarness Bridge
- `OPENHARNESS_BRIDGE.md`
- `docs/OPENHARNESS_BRIDGE_OPEN_ITEMS.md`
- `docs/OPENHARNESS_BRIDGE_INDEX.md`
