# Upgrade Checklist for Moving to v1.0.1 beta

This checklist is meant to keep the beta upgrade focused on the public baseline only.  
If you want the `v1.0.1 beta` minimal effect, overwrite the shared foundation, standard docs, and release resources. Do not overwrite your own business code or project-specific customizations.

## 1. Files to overwrite

If your goal is to align the repository with the `v1.0.1 beta` public baseline, overwrite these files and directories:

### Root release-facing files

- `README.md`
- `README.en.md`
- `VERSION_ROADMAP.md`
- `VERSION_ROADMAP.en.md`
- `GITHUB_RELEASE.md`
- `GITHUB_RELEASE.en.md`

### Documentation center

- `docs/README.md`
- `docs/README.en.md`
- `docs/INDEX.md`
- `docs/INDEX.en.md`
- `docs/HARNESS_SPEC.md`
- `docs/HARNESS_SPEC.en.md`
- `docs/GITHUB_RELEASE.md`
- `docs/GITHUB_RELEASE.en.md`
- `docs/GITHUB_PUBLISH_GUIDE.md`
- `docs/VERSION_ROADMAP.md`
- `docs/VERSION_ROADMAP.en.md`
- `docs/EXTENSION_POINTS.md`
- `docs/EXTENSION_POINTS.en.md`
- `docs/AI_CHECKLIST.md`
- `docs/AI_OPERATIONS.md`
- `docs/AI_OPERATIONS.en.md`

### Tooling and standard entry points

- `tools/init_module.py`
- `tools/apply_harness.py`
- `tools/validate_module.py`
- `.openclaw_skill/SKILL.md`
- `.openclaw_skill/scripts/`
- `.openclaw_skill/templates/`
- `.openclaw_skill/references/`
- `.openclaw_skill/profiles/`

### Extension surfaces and defaults

- `profiles/`
- `templates/`
- `examples/hello_world/`
- `examples/local_extension/`, if you want the local extension example to be part of the beta baseline

### Release resources

- `release/v1.0.1-beta/`

## 2. Files to keep untouched

Do not overwrite the following unless you explicitly want to remove project-specific custom work:

- your own business module directories
- project-specific configuration files
- project-specific test files
- `.env`, keys, credentials, and local secrets
- CI or release workflows that are already tailored to your project
- any source directory that already contains application logic

If your repository has directories like these, treat them as custom code first:

- `modules/`
- `src/`
- `app/`
- `service/`
- `worker/`
- `domain/`

If they already contain business logic, preserve them.

## 3. Upgrade strategies

### Option A: Align only the beta baseline

Use this if you only want the docs, templates, tools, skill package, and release notes aligned with `v1.0.1 beta`.

Overwrite:

- root README files
- `docs/`
- `tools/`
- `.openclaw_skill/`
- `profiles/`
- `templates/`
- `release/v1.0.1-beta/`

### Option B: Bring the full minimal baseline over

Use this if you want a fresh install or a new branch to behave like the beta minimal baseline right away.

Overwrite:

- everything in Option A
- `examples/hello_world/`
- `examples/local_extension/`
- any shared core directory if your repository has one

### Option C: Keep your customization and only sync the common foundation

Use this if the repository already has significant custom work and you only want the public infrastructure updated.

Overwrite:

- `README.md` / `README.en.md`
- `docs/`
- `tools/`
- `.openclaw_skill/`
- `profiles/`
- `templates/`
- `release/v1.0.1-beta/`

Do not overwrite:

- your own business directories
- your own custom modules
- your own tests and configs

## 4. Recommended order

1. Overwrite docs and release notes first
2. Then sync `tools/` and `.openclaw_skill/`
3. Then sync `profiles/` and `templates/`
4. Optionally sync the example directories
5. Finally check that `release/v1.0.1-beta/` is complete

## 5. Post-upgrade checks

- Is the version in `README` set to `v1.0.1 beta`?
- Do `VERSION_ROADMAP` and the docs still mention the old version anywhere?
- Are `docs/INDEX.md` and `docs/HARNESS_SPEC.md` still using the old phrasing?
- Are `tools/validate_module.py`, `tools/apply_harness.py`, and `tools/init_module.py` still aligned with the skill package?
- Are `profiles/` and `templates/` still lightweight presets instead of a thick policy system?
- Does `release/v1.0.1-beta/` still include bilingual version descriptions and release resources?

## 6. One-line rule

If you want the `v1.0.1 beta` minimal effect, overwrite the public baseline and release resources first.  
If you want to keep your own customization, do not overwrite your business code and project-specific files.
