# Release Playbook

This document is the primary release workflow for future versions of this repository.  
The goal is not to redesign the process every time, but to keep version wording, file synchronization, validation, packaging, and release publication on one repeatable track.

## 1. Align the wording before publishing

Before every release, confirm that these concepts are aligned:

- The repository homepage should show the current version by default
- If the current version is shown as `v1.0.1 beta`, the homepage, documentation hub, roadmap, release page, and version description should all match
- `v1.0.0` should remain only as the historical anchor
- The default consistency mode should stay `soft`
- Extensions should remain example-first and project-local
- Keep version display and Git tag naming separate:
  - Display wording: `v1.0.1 beta`
  - Git tag: `v1.0.1-beta`

## 2. Files that must be synchronized

For every new release, sync these files first:

### 1. Repository homepage

- `README.md`
- `README.en.md`

### 2. Documentation hub

- `docs/README.md`
- `docs/README.en.md`
- `docs/INDEX.md`
- `docs/INDEX.en.md`
- `docs/VERSION_ROADMAP.md`
- `docs/VERSION_ROADMAP.en.md`
- `docs/GITHUB_RELEASE.md`
- `docs/GITHUB_RELEASE.en.md`
- `docs/GITHUB_PUBLISH_GUIDE.md`

### 3. Release package

- `release/v1.0.x-beta/README.md`
- `release/v1.0.x-beta/README.en.md`
- `release/v1.0.x-beta/VERSION_DESCRIPTION.zh.md`
- `release/v1.0.x-beta/VERSION_DESCRIPTION.en.md`
- `release/v1.0.x-beta/GITHUB_RELEASE.zh.md`
- `release/v1.0.x-beta/GITHUB_RELEASE.en.md`
- `release/v1.0.x-beta/DISPLAY_PAGE.zh.md`
- `release/v1.0.x-beta/DISPLAY_PAGE.en.md`
- `release/v1.0.x-beta/PUBLISH_CHECKLIST.zh.md`
- `release/v1.0.x-beta/PUBLISH_CHECKLIST.en.md`
- `release/v1.0.x-beta/UPGRADE_CHECKLIST.zh.md`
- `release/v1.0.x-beta/UPGRADE_CHECKLIST.en.md`
- `release/v1.0.x-beta/MANIFEST.md`

### 4. Version roadmap

- `docs/VERSION_ROADMAP.md`
- `docs/VERSION_ROADMAP.en.md`

## 3. Recommended order

Do not jump around. Follow this order:

1. Set the version number and homepage wording
2. Sync the homepage and documentation hub
3. Sync the version description, display page, upgrade checklist, and release body
4. Run validation commands
5. Create the Git tag
6. Publish the GitHub Release
7. Upload the release asset bundle

## 4. Fixed validation commands

Run these before publishing:

```bash
python tools/validate_module.py examples/hello_world --strict --profile python-service
python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service
python -m py_compile tools/init_module.py tools/apply_harness.py tools/validate_module.py
python examples/local_extension/harness/run_harness.py
```

## 5. Release body rules

The release body should keep a stable shape:

- Start with a short summary of what changed
- State the version being released
- Link to the version description
- List the validation commands
- State the risk boundaries
- State the rollback anchor

If the release is meant to show a historical baseline, use historical-baseline wording.  
If it is a new beta release, keep the beta-freeze wording.

## 6. Upgrade and rollback wording

- `v1.0.0` stays as the historical anchor
- The default display version is written as `v1.0.1 beta`
- Git tags use the hyphenated form: `v1.0.1-beta`
- If the next release changes, update all three together:
  - homepage
  - documentation hub
  - release package

## 7. When a release is ready

Release only when all of these are true:

- Homepage and documentation hub match
- Version description is complete
- Release assets are packaged
- Validation commands pass
- The current wording does not conflict with the historical version

## 8. One-line takeaway

For each future release, align the wording first, then sync the resources, then validate, then publish. That keeps releases repeatable and avoids rebuilding the process from scratch each time.
