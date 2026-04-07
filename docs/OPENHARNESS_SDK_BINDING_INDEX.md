# OpenHarness SDK Binding Index

This index is the work-order map for the OpenHarness SDK binding line.

## Stable Inputs
- `OPENHARNESS_SDK_BINDING.md`
- `OPENHARNESS_BRIDGE.md`
- `adapters/openharness_sdk_binding.py`
- `adapters/openharness_bridge.py`
- `adapters/openharness_sdk_binding.sample.ts`
- `scripts/openharness_validate_transport.py`
- `scripts/openharness_sdk_binding_export.py`
- `examples/openharness_app/`
- `docs/OPENHARNESS_EXTERNAL_VERIFY.md`
- `OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.md`

## Still Open
- `docs/OPENHARNESS_SDK_BINDING_OPEN_ITEMS.md`
- live `@openharness/core` package binding
- non-process validate transport
- provider registration mapping
- middleware registration mapping
- SDK-binding-specific validation matrix

## Recommended Order
1. Keep the bridge export stable.
2. Keep the SDK binding shell narrow.
3. Keep the process transport stable.
4. Validate the TypeScript sample against a real OpenHarness app when available.
5. Only then consider a non-process transport for `harness_validate`.
6. Only then widen the SDK binding if a real integration proves the need.
