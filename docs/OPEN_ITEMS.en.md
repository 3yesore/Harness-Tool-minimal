# Open Items

This document tracks the intentionally unfinished parts of the current base.

## Left open on purpose
- The adapter layer is protocol-first, not a full runtime yet
- OS / multi-agent / external project integration remains bridge-scoped
- The adapter validation matrix remains minimal
- Adapter pack/versioning rules remain to be hardened only when needed

## Why this stays open
- To preserve extension space
- To avoid premature platformization
- To keep the core thin while the boundary hardens

## How to use this document
- Treat it as the handoff note for the next upgrade round
- Do not move these items into `core` unless they become contract-level requirements
- Expand the adapter layer only after a sample proves the need
