# OpenHarness Bridge Open Items

## Kept Open On Purpose
- Bridge input is still document-first, not runtime-first.
- No live OpenHarness provider mapping exists yet.
- No live OpenHarness middleware hook mapping exists yet.
- No real OpenHarness skill or `AGENTS.md` registration flow is finalized yet.
- No bridge-specific validation matrix exists yet.
- The bridge is verified through an external app, but only through the current process-shell path.

## Why This Stays Open
- To keep `harness_tool` upstream and stable.
- To avoid turning `harness_tool` into an OpenHarness host runtime.
- To force the bridge to stay narrow and evidence-driven.

## Upgrade Rule
- Do not move bridge logic into `core`.
- Do not widen the bridge until a real OpenHarness integration path proves the need.
- If a new bridge capability is proposed, document it here first.
