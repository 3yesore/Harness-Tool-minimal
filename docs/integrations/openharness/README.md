# OpenHarness Integration

OpenHarness is an external runtime connected to this repository through a bridge. It is not owned by `harness_core`.

Start here if you want to understand the current integration shape.

## What this integration is

- a narrow bridge from Harness Tool into an external runtime
- a binding and transport path for `harness_validate`
- a context-injection path for OpenHarness-facing usage
- a verified compatibility path with internal and external examples

## What is verified

- bridge and binding documents exist
- process transport is implemented
- context payload and injection material exist
- internal OpenHarness example exists
- external verification notes exist

## What stays outside core

- runtime ownership
- provider lifecycle ownership
- middleware lifecycle ownership
- full session and conversation integration

## Read next

- [Bridge](../../OPENHARNESS_BRIDGE.md)
- [SDK binding](../../OPENHARNESS_SDK_BINDING.md)
- [Provider / middleware contract](../../OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.md)
- [External verification](../../OPENHARNESS_EXTERNAL_VERIFY.md)
- [Bridge open items](../../OPENHARNESS_BRIDGE_OPEN_ITEMS.md)
- [SDK binding open items](../../OPENHARNESS_SDK_BINDING_OPEN_ITEMS.md)
- [Provider / middleware open items](../../OPENHARNESS_PROVIDER_MIDDLEWARE_OPEN_ITEMS.md)
