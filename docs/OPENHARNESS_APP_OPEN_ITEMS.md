# OpenHarness App Open Items

## Kept Open On Purpose
- The example does not perform a real model call.
- Provider registration is not exercised.
- Middleware registration is not exercised.
- Session and Conversation flows are not exercised.
- Only the process transport is validated.
- The external app template is verified, but only against the current smoke scope.

## Why This Stays Open
- To keep the example focused on bridge, binding, and transport.
- To avoid widening the example into a full runtime demo.
- To keep `harness_tool` upstream and contract-first.

## Upgrade Rule
- Do not move OpenHarness runtime ownership into this repo.
- Do not expand the example into a provider or middleware demo unless a real integration requires it.
- If a new validation target is added, record it here first.
