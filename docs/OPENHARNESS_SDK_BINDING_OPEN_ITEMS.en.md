# OpenHarness SDK Binding Open Items

## Kept Open On Purpose
- No live in-process `@openharness/core` package call is wired yet.
- The TypeScript sample has been verified in a repo-external app, but not against a full upstream OpenHarness example repository.
- No provider registration mapping is finalized yet.
- No middleware registration mapping is finalized yet.
- No transport other than the local process shell is defined for calling `harness_validate`.
- No SDK-binding-specific validation matrix exists yet.

## Why This Stays Open
- To keep `harness_tool` upstream and stable.
- To keep `openharness_bridge` narrow.
- To avoid turning the SDK binding shell into a hosted runtime layer.

## Upgrade Rule
- Keep the SDK binding outside `harness_core`.
- Do not move binding logic into the bridge unless the split becomes redundant.
- Do not widen the binding until a real OpenHarness SDK integration proves the need.
