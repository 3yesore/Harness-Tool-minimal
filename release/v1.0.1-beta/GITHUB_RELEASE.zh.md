# Harness Tool Minimal v1.0.1 beta

本次更新简而言之是一些基线加固工作和开放了一些标准化拓展，并且都是在 minimal 基础上做的稳定性建设。但目前仍建议在小项目小模块的开发初期使用。具体更新内容请移步（[VERSION_DESCRIPTION.zh.md](VERSION_DESCRIPTION.zh.md)），后续会根据我实际测试推出更多的扩展和大结构更新，届时会根据社区反响尝试往大型项目的方向推进，敬请期待，欢迎讨论！

## 发布摘要

- 保持最小闭环：`init / apply / validate`
- 保持标准化模块入口：`INDEX.md`、`SPEC.md`、`CHANGELOG.md`
- 保持轻量扩展面：`profiles/`、`templates/`、`.openclaw_skill/`
- 保持 GitHub Actions 基础验证
- 保持中文主页 + 英文镜像的发布形式

## 验证命令

```bash
python tools/validate_module.py examples/hello_world --strict --profile python-service
python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service
python -m py_compile tools/init_module.py tools/apply_harness.py tools/validate_module.py
```

## 发布说明

- 这是 `v1.0.1 beta` 的冻结发布。
- 回滚锚点：`v1.0.0`
- 适合小项目、小模块、开发初期使用。
- 后续会根据测试和反馈决定是否推进更大结构。

