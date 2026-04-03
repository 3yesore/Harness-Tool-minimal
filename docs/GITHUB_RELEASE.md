# GitHub 发布页说明

这是测试仓库整理后的发布准备页。发布前先把根目录收干净，确认示例模块和 skill 包都能通过验证，再同步到 GitHub。

## 发布前检查

1. 运行仓库验证脚本。
2. 确认 `examples/hello_world` 仍然通过冒烟测试。
3. 确认没有临时文件、缓存文件或本地构建产物留在仓库里。
4. 确认 `.openclaw_skill/` 与当前实现同步。

推荐检查命令：

```bash
python tools/validate_module.py examples/hello_world --strict --profile python-service
python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service
python -m py_compile tools/init_module.py tools/apply_harness.py tools/validate_module.py
```

## 发布到 GitHub

```bash
git status --short
git add .
git commit -m "Prepare harness tool release"
git push
```

如果发布仓库和测试仓库不是同一个目录，先把确认过的内容同步过去，再重复上面的验证。

## 推荐发布说明

```markdown
## Harness Tool Minimal v1.0

Highlights:
- modular handoff flow with `INDEX.md`, `SPEC.md`, and `CHANGELOG.md`
- runnable smoke-test validation
- profile-based rule presets
- bundled OpenClaw / Codex skill package
- reference examples in `examples/`

Skill install:
- download the ZIP archive directly from GitHub
- copy `.openclaw_skill` into your local skill directory
- if your skill manager supports name-based install, publish the package there as well

Validation:
- `python tools/validate_module.py examples/hello_world --strict --profile python-service`
- `python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service`
```

## 发布后

1. 打上版本标签，例如 `v1.0.0`。
2. 补一条简短的 GitHub Release 描述。
3. 确认 README、release 页和 skill 包口径一致。
4. 如果路线图变了，更新 `VERSION_ROADMAP.md`。
