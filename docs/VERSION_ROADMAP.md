# Harness Tool Version Roadmap

## Current Version

- `v1.0.1 beta`
- Status: frozen minimal baseline
- Focus: thin kernel, hard contract, explicit extension surface, isolated rollback anchor

## What v1.0.1 beta Includes

- `HARNESS_SPEC.md`
- `tools/init_module.py`
- `tools/apply_harness.py`
- `tools/validate_module.py`
- `templates/`
- `profiles/`
- `examples/hello_world/`
- `.openclaw_skill/`
- `RELEASE_NOTES_v1.0.1_beta.md`
- OpenHarness-compatible bridge and external verification

## What the Beta Freeze Means

- keep the core small
- do not turn validation into a heavy analysis platform
- do not turn profiles into a policy engine
- do not turn templates into a tutorial system
- keep extension and override explicit and safe
- keep OpenHarness integration in the bridge layer

## Planned Direction

### v1.1

Goal: extend the same harness kernel with clearer project-local customization.

Likely additions:

- richer project-local override
- more profile presets
- safer apply/update path
- clearer bridge-side validation reporting

### v2.0

Goal: broaden the same contract without losing the minimal baseline.

Likely additions:

- better source discovery
- additional language presets
- broader validation reporting
- possibly richer external integration evidence, still outside `core`

## Release Policy

- Keep `v1.x` backward compatible with the current module layout
- Keep the skill package synced with repository behavior
- Preserve the `1.0.1 beta` baseline as the rollback anchor

## Notes

- This roadmap describes intent, not a promise of immediate implementation.
- If the implementation changes, update this file together with `INDEX.md` and `HARNESS_SPEC.md`.
