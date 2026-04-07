# Work Index

This index is not a full freeze. It tells the next organizer what should be handled first, and what should remain open for now.

## Current Priority

### Layer 1: Core already frozen
Keep and organize to the final protocol:
- `CORE_PROTOCOL.md`
- `ADAPTER_PROTOCOL.md`
- `EXTENSION_PROTOCOL.md`
- `harness_core/`
- `tools/`

### Layer 2: Main entry documents
Keep the top-level docs aligned with the protocol map:
- `README.md`
- `README.en.md`
- `INDEX.md`
- `INDEX.en.md`
- `HARNESS_SPEC.md`
- `HARNESS_SPEC.en.md`
- `VERSION_ROADMAP.md`
- `VERSION_ROADMAP.en.md`
- `DESIGN_REVIEW.md`
- `AI_CHECKLIST.md`
- `GITHUB_RELEASE.md`

### Layer 3: Extension surface
Keep these visible, but do not thicken them prematurely:
- `profiles/`
- `templates/`
- `adapters/`
- `examples/local_extension/`
- `.openclaw_skill/`

### Layer 4: Open items
Keep these as docs and samples for now, not core:
- `docs/OPEN_ITEMS.md`
- `docs/OPEN_ITEMS.en.md`
- `docs/CURRENT_CHANGESET_INDEX.md`
- `docs/CURRENT_CHANGESET_INDEX.en.md`
- `docs/FREEZE_GROUPS.md`
- `docs/FREEZE_GROUPS.en.md`
- `adapters/sample_usage.md`
- `adapters/workspace.py`
- future adapter samples

## Suggested Organization Order

1. Organize `core` protocol files and `harness_core/`
2. Organize the main entry documents
3. Organize `adapters/` samples and docs
4. Organize `profiles/`, `templates/`, and `examples/`
5. Revisit `.openclaw_skill/` only if a mirror update is needed

## Freeze Execution Entry

- responsibility index: `docs/CURRENT_CHANGESET_INDEX.en.md`
- commit grouping index: `docs/FREEZE_GROUPS.en.md`

## Retention Rules

- Keep unfinished items in `docs/OPEN_ITEMS.md`
- If you are doing final cleanup, start with `docs/CURRENT_CHANGESET_INDEX.en.md`
- If you are doing final commit splitting, follow `docs/FREEZE_GROUPS.en.md`
- Keep samples under `adapters/` or `examples/`
- Do not move open items into `core`
- Do not narrow extension space just to make the tree look tidy

## How to Use This Index

- Read the priority layers first
- Then organize in order
- If something is still uncertain, keep it open
- Only move a topic out of open items once it becomes part of the protocol

## OpenHarness App
- `examples/openharness_app/`
- `docs/OPENHARNESS_APP_OPEN_ITEMS.en.md`
- `docs/OPENHARNESS_APP_INDEX.en.md`
- `OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.en.md`
- `docs/OPENHARNESS_PROVIDER_MIDDLEWARE_OPEN_ITEMS.en.md`
- `docs/OPENHARNESS_PROVIDER_MIDDLEWARE_INDEX.en.md`
