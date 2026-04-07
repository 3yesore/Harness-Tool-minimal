# OpenHarness SDK Binding

## Position
This binding sits above the OpenHarness bridge and below any real OpenHarness SDK
runtime usage.

- `harness_tool` stays the upstream contract provider
- `openharness_bridge` stays the narrow translation layer
- this SDK binding stays a registration shell

It does not host OpenHarness inside `harness_tool`.

## Goal
The goal is to expose one stable, SDK-facing surface that can be consumed by a
real OpenHarness integration without widening `core`.

## What It Exports
The binding exports:

- bridge metadata
- transport metadata
- tool definition for `harness_validate`
- context payload
- provider hints
- middleware hints
- agent context injection text
- skill snippet
- tool call example
- a copyable TypeScript sample
- a local process transport script path

## Local Entry
- `adapters/openharness_sdk_binding.py`
- `adapters/openharness_sdk_binding.sample.ts`
- `scripts/openharness_validate_transport.py`

## Narrow Binding Rule
- do not import or host OpenHarness in `harness_core`
- do not move runtime lifecycle into adapters
- do not turn the binding into a generic agent platform
- do not widen inputs beyond the current bridge surface unless a real integration proves the need

## Current Shape
The binding currently packages:

- `export_openharness_integration(...)`
- `build_registration_contract(...)`
- `render_typescript_sample(...)`
- `export_openharness_sdk_binding(...)`

## Transport
The first real transport is a local Python process transport:

- script: `scripts/openharness_validate_transport.py`
- transport kind: `process`
- direction: OpenHarness runtime -> Python bridge process -> `harness_validate`

This is intentionally narrow. It proves live tool transport without moving SDK
runtime ownership into `harness_tool`.

## Still Open
- real in-process `@openharness/core` package binding is not wired yet
- provider registration shape is still local and static
- middleware registration remains hint-only
- no transport other than the local process shell is defined yet

## Related Documents
- `OPENHARNESS_BRIDGE.md`
- `OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.md`
- `docs/OPENHARNESS_BRIDGE_OPEN_ITEMS.md`
- `docs/OPENHARNESS_BRIDGE_INDEX.md`
- `docs/OPENHARNESS_EXTERNAL_VERIFY.md`
- `docs/OPENHARNESS_SDK_BINDING_OPEN_ITEMS.md`
- `docs/OPENHARNESS_SDK_BINDING_INDEX.md`
