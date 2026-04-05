# 发布检查清单

## 发布前

- 确认 `README.md` 是中文主页，`README.en.md` 是英文镜像
- 确认 `VERSION_DESCRIPTION.zh.md` 和 `VERSION_DESCRIPTION.en.md` 口径一致
- 确认 `GITHUB_RELEASE.zh.md` 的第一条保留你提供的更新摘要
- 确认版本号统一为 `v1.0.1 beta` / `v1.0.1-beta`
- 确认不再混用 `v1.0.0`

## 验证命令

```bash
python tools/validate_module.py examples/hello_world --strict --profile python-service
python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service
python -m py_compile tools/init_module.py tools/apply_harness.py tools/validate_module.py
```

## GitHub 发布

```bash
git status --short
git add .
git commit -m "Prepare v1.0.1 beta release"
git tag v1.0.1-beta
git push origin main
git push origin v1.0.1-beta
```

## 发布后

- 检查 GitHub Release 标题和正文是否正确
- 检查 tag 是否指向当前 `main` 提交
- 检查是否把 `v1.0.0` 和 `v1.0.1 beta` 混在一起

