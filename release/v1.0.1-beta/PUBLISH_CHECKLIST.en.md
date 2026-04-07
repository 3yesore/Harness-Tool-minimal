# Release Checklist

Before publishing `v1.0.1 beta`, confirm each item below.

## Code and Validation

- [ ] `python tools/validate_module.py examples/hello_world --strict --profile python-service` passes
- [ ] `python tools/validate_module.py examples/local_extension --strict --profile default` passes
- [ ] `python tools/validate_module.py examples/openharness_app --strict --profile default` passes
- [ ] `python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service` passes
- [ ] `npm run build` in `C:/Users/Y2516/Desktop/openharness_app_external_verify` passes
- [ ] `npm run smoke` in `C:/Users/Y2516/Desktop/openharness_app_external_verify` passes

## Release Materials

- [ ] `RELEASE_NOTES_v1.0.1_beta.md` has been updated
- [ ] `release/v1.0.1-beta/VERSION_DESCRIPTION.zh.md` has been updated
- [ ] `release/v1.0.1-beta/VERSION_DESCRIPTION.en.md` has been updated
- [ ] `release/v1.0.1-beta/GITHUB_RELEASE.zh.md` has been updated
- [ ] `release/v1.0.1-beta/GITHUB_RELEASE.en.md` has been updated
- [ ] the release wording matches the current repository state

## Repository State

- [ ] freeze groups have been committed in batches
- [ ] no temporary files or cache directories remain
- [ ] `examples/openharness_app/node_modules/` is not tracked
- [ ] `harness_core/` remains thin and does not grow into a runtime platform
- [ ] OpenHarness compatibility remains in the bridge / binding layer
- [ ] default consistency remains `soft`

## After Release

- [ ] tag the release as `v1.0.1-beta`
- [ ] keep `v1.0.0` as the rollback anchor
- [ ] check that README, spec, skill mirror, and bridge docs still match the published behavior
