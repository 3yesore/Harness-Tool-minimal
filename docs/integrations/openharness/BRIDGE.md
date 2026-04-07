# OpenHarness Bridge

## Position
`harness_tool` remains the upstream contract and project-structure provider.
`OpenHarness` remains an external agent runtime and orchestration system.

This bridge exists to connect the two without turning `harness_tool` into an
OpenHarness host runtime.

## Bridge Goal
The first bridge goal is narrow:

- translate `harness_tool` contract context into OpenHarness-friendly input
- expose `validate` as a preflight or contract gate
- translate OpenHarness execution results back into harness-friendly output

## Upstream / Downstream Split
- `harness_tool` upstream provides:
  - `INDEX.md`
  - `SPEC.md`
  - `CHANGELOG.md`
  - marker summaries
  - `validate` results
  - contract-safe next actions and patch drafts
- `OpenHarness` downstream provides:
  - `Agent`
  - `Session`
  - `Middleware`
  - `Subagents`
  - `Skills`
  - `Providers`

## Minimal Bridge Inputs
The first bridge version should only consume:

- module identity
- `INDEX.md` summary
- `SPEC.md` summary
- marker summary
- latest `ValidationResult`

### Payload Shape
```json
{
  "bridge_version": "v1.0.1 beta",
  "source": "harness_tool",
  "target": "openharness",
  "module_name": "example_module",
  "index_summary": "...",
  "spec_summary": "...",
  "marker_summary": {},
  "validation_result": {},
  "allowed_primitives": ["Agent", "Session", "Middleware", "Subagents", "Skills", "Providers"]
}
```

## Minimal Bridge Outputs
The first bridge version should only emit:

- OpenHarness-ready context payload
- bridge notes and warnings
- normalized task result summary
- patch draft or next-action hints

### Result Shape
```json
{
  "status": "success",
  "summary": "...",
  "notes": [],
  "warnings": [],
  "patch_draft": [],
  "next_actions": [],
  "source_runtime": "openharness"
}
```

## Mapping Direction
- `INDEX.md` / `SPEC.md` / markers -> OpenHarness context injection
- `validate` -> preflight gate or tool call
- OpenHarness result -> harness-friendly summary

## First Concrete Entry Points

### 1. Validate Tool
The bridge exposes Harness validation as a callable tool envelope:

- tool name: `harness_validate`
- input:
  - `module_path`
  - `profile`
  - `strict`
- output:
  - `status`
  - `errors`
  - `warnings`
  - `notes`
  - `next_actions`
  - `patch_draft`
  - `stage_trace`
  - `rendered_text`

### 2. Context Generator
The bridge exposes a real module-to-context generator:

- source:
  - `INDEX.md`
  - `SPEC.md`
  - marker registry
  - latest `ValidationResult`
- output:
  - OpenHarness-ready context payload
  - module summary
  - marker summary
  - validation snapshot

### 3. Registration Bundle
The bridge also exposes a minimal registration bundle:

- `tool_definition`
- `context_payload`
- `bridge` metadata

This bundle is intended to be the narrow handoff shape for a future real
OpenHarness integration path.

### 4. Agent Context Injection
The bridge exposes a plain-text context injection block for an OpenHarness
agent. It includes:

- module identity
- index summary
- spec summary
- marker summary
- validation snapshot

### 5. Skill Snippet
The bridge also exposes a minimal skill-style snippet that can be injected into
an OpenHarness skill or `AGENTS.md`-style instruction layer. It keeps the
contract-first rule explicit and instructs the agent to run `harness_validate`
before non-trivial changes.

### 6. Integration Export
The bridge now exposes a harder integration surface that packages the narrow
handoff into one export:

- bridge metadata
- module metadata
- tool definition
- OpenHarness-ready context payload
- provider hints
- middleware hints
- agent context injection text
- skill snippet
- example tool call
- reference pointers to bridge docs and open items

The local helper is:

- `export_openharness_integration(workspace_path, module_path, ...)`

This remains bridge-only. It does not host or bootstrap an OpenHarness runtime.

### 7. Provider Hints
The bridge exposes narrow provider hints for an external OpenHarness runtime:

- provider ownership stays outside `harness_tool`
- the provider should treat `harness_validate` as an external process-backed tool
- the provider should consume the context payload as upstream module context, not runtime state

### 8. Middleware Hints
The bridge also exposes narrow middleware hints:

- `preflight_validate`
- `context_injection`
- `postflight_result_normalization`

These are hints only. They do not register or host OpenHarness middleware.

## Explicit Non-Goals
The first bridge version must not:

- host OpenHarness runtime inside `harness_core`
- manage OpenHarness session persistence
- own OpenHarness provider lifecycle
- implement UI streaming
- implement full subagent orchestration

## Current Local Entry
- `adapters/openharness_bridge.py`

## Current Status
- bridge-first
- protocol-first
- runtime-light
- still incomplete

## Related Documents
- `ADAPTER_PROTOCOL.md`
- `CORE_PROTOCOL.md`
- `EXTENSION_PROTOCOL.md`
- `OPENHARNESS_SDK_BINDING.md`
- `OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.md`
- `docs/OPENHARNESS_BRIDGE_OPEN_ITEMS.md`
- `docs/OPENHARNESS_BRIDGE_INDEX.md`
