# OpenHarness App Index

This index is the work-order map for the repo-local OpenHarness app example.

## Stable Inputs
- `examples/openharness_app/package.json`
- `examples/openharness_app/tsconfig.json`
- `examples/openharness_app/src/main.ts`
- `examples/openharness_app/src/main.py`
- `examples/openharness_app/src/smoke.ts`
- `examples/openharness_app/src/types.ts`
- `examples/openharness_app/tests/smoke.py`
- `scripts/openharness_sdk_binding_export.py`
- `scripts/openharness_validate_transport.py`

## Still Open
- `docs/OPENHARNESS_APP_OPEN_ITEMS.en.md`
- real model invocation
- provider registration validation
- middleware registration validation
- non-process transport
- external app template expansion beyond current smoke scope

## Recommended Order
1. Keep the example buildable.
2. Keep the example smoke passing.
3. Keep the example pinned to bridge, binding, and transport only.
4. Only expand the app if a real OpenHarness integration requires it.
