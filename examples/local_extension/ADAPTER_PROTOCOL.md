# Local Adapter Protocol Envelope

This module intentionally keeps a small adapter envelope so `validate` can
verify the shell without pulling adapter runtime concerns into `harness_core`.

## What stays frozen
- protocol version
- lifecycle shape
- capability declaration
- compatibility hint

## What stays open
- internal adapter implementation
- OS / multi-agent integration details
- project-specific workflow wiring

## Boundary
- adapter translates
- core validates
- extension customizes
