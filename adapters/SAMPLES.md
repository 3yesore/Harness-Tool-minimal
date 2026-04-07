# Adapter Samples Overview

This document is the directory map for adapter examples and future sample slots.
It is intentionally small and protocol-first.

## Current Layout
- `protocol.py`:
  - Minimal adapter protocol envelope.
  - Defines version, lifecycle, and the smallest shared data types.
- `os.py`:
  - OS-level adapter shell template.
  - Shows how a project can translate workspace or system capabilities into a harness-friendly envelope.
- `multi_agent.py`:
  - Multi-agent adapter shell template.
  - Shows how a project can coordinate multiple agents without moving orchestration into `harness_core`.
- `openharness_bridge.py`:
  - OpenHarness bridge shell template.
  - Shows how a project can map OpenHarness primitives into the local envelope without turning Harness Tool into an OpenHarness host.
- `openharness_sdk_binding.py`:
  - OpenHarness SDK binding shell.
  - Packages the bridge export into an SDK-facing registration contract without hosting runtime ownership.
- `openharness_sdk_binding.sample.ts`:
  - Copyable TypeScript binding sample.
  - Shows how a real OpenHarness app can consume the exported bridge surface.
- `scripts/openharness_validate_transport.py`:
  - Local Python process transport for `harness_validate`.
  - Provides a real runtime-callable boundary without moving transport logic into `harness_core`.
- `project_bridge.py`:
  - External project bridge adapter shell template.
  - Shows how a project can wrap an external open-source project without moving bridge logic into `harness_core`.
- `workspace.py`:
  - Workspace-focused adapter sample.
  - Shows how a local workspace can be translated into a harness-friendly context.
- `workflow.py`:
  - Workflow-focused adapter sample.
  - Shows how staged coordination can stay thin while still being explicit.
- `sample_usage.md`:
  - Minimal usage notes for importing and calling the sample adapters.

## Template For New Samples
Use the same shape when adding a new adapter sample:

1. Add a module next to the existing samples.
2. Re-export or import the protocol envelope from `protocol.py`.
3. Expose a small public adapter class or factory.
4. Keep the adapter importable without requiring a full runtime platform.
5. Add a short README note that says what the sample demonstrates.
6. If the sample targets a real external runtime, keep the SDK-facing shell separate from the bridge shell.

## Reserved Future Slots
These names are intentionally kept open for later expansion:
- `orchestration.py` for future high-level coordination samples.

## What Must Stay Out Of Core
- No adapter runtime platform in `harness_core`.
- No project-specific logic in the protocol envelope.
- No hidden lifecycle beyond the documented sample contract.
- No validation of internal adapter behavior beyond shell checks.

## Handoff Rule
If a sample becomes stable and reusable, upgrade it in the adapter layer first.
Do not promote it into `core` unless the contract itself needs to change.
