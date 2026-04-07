# OpenHarness Provider / Middleware Bridge Contract

## Position
This contract keeps provider and middleware handling inside the OpenHarness-side
bridge surface.

`harness_tool` stays upstream and continues to provide:

- contract files
- marker summaries
- validation results
- context payloads

This contract does not move provider lifecycle or middleware registration into
`harness_core`.

## Scope
This page only defines the narrow bridge contract for:

- `provider_hints`
- `middleware_hints`

It does not define runtime ownership, provider bootstrapping, middleware
implementation, or session orchestration.

## Provider Hints
`provider_hints` are advisory bridge metadata for an external OpenHarness
runtime.

### Required fields
- `provider_mode`
- `recommended_provider_role`
- `bridge_constraints`
- `context_payload`

### Current shape
```json
{
  "provider_mode": "external-runtime-owned",
  "recommended_provider_role": "model-and-tool-host",
  "bridge_constraints": [
    "Do not move provider lifecycle into harness_tool.",
    "Treat harness_validate as an external process-backed tool.",
    "Use harness_tool context payload as upstream project context, not as provider state."
  ],
  "context_payload": {}
}
```

### Contract meaning
- Provider ownership stays outside `harness_tool`.
- `harness_validate` is exposed as a process-backed bridge tool, not a provider-owned primitive.
- The provider consumes `context_payload` as upstream module context, not as mutable runtime state.

## Middleware Hints
`middleware_hints` are advisory bridge metadata for an external OpenHarness
runtime.

### Required fields
- `middleware_mode`
- `recommended_hooks`
- `bridge_constraints`
- `validation_snapshot`

### Current shape
```json
{
  "middleware_mode": "external-runtime-owned",
  "recommended_hooks": [
    "preflight_validate",
    "context_injection",
    "postflight_result_normalization"
  ],
  "bridge_constraints": [
    "Run harness_validate before non-trivial file changes.",
    "Inject INDEX/SPEC/marker summaries before task execution.",
    "Normalize downstream output back into summary, notes, warnings, patch_draft, and next_actions."
  ],
  "validation_snapshot": {
    "status": "success",
    "errors": 0,
    "warnings": 0
  }
}
```

### Contract meaning
- Middleware ownership stays outside `harness_tool`.
- The bridge only recommends hook order.
- Validation remains a contract gate.
- Result normalization remains a bridge concern, not a core concern.

## Required Boundaries
- Do not register providers inside `harness_core`.
- Do not register middleware inside `harness_core`.
- Do not treat `provider_hints` or `middleware_hints` as executable core state.
- Do not widen these hints into a host runtime contract.

## Allowed Uses
- Feed the hints into an OpenHarness app bootstrap layer.
- Document expected provider/middleware ordering.
- Keep runtime-specific decisions in the external OpenHarness app.

## Explicit Non-Goals
- Provider lifecycle management
- Middleware implementation ownership
- Session persistence wiring
- Conversation state wiring
- UI streaming integration

## Current Sources
- `adapters/openharness_bridge.py`
- `adapters/openharness_sdk_binding.py`
- `docs/OPENHARNESS_EXTERNAL_VERIFY.md`

## Open Items
- Live provider registration wiring remains external.
- Live middleware registration wiring remains external.
- Non-process transport remains open.
- Full session/conversation validation remains open.

## Related Documents
- `OPENHARNESS_BRIDGE.md`
- `OPENHARNESS_SDK_BINDING.md`
- `docs/OPENHARNESS_PROVIDER_MIDDLEWARE_OPEN_ITEMS.md`
- `docs/OPENHARNESS_PROVIDER_MIDDLEWARE_INDEX.md`
