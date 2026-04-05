# Harness Tool Minimal v1.0.1 beta

本次更新简而言之是围绕 minimal 基线做了一轮加固，并开放了若干标准化扩展入口，但整体仍然以稳定性、交接性和工程边界收口为主。  
如果你需要完整的版本说明、验证范围和风险边界，请移步：[VERSION_DESCRIPTION.zh.md](VERSION_DESCRIPTION.zh.md)。  
当前版本仍然更适合小项目、小模块和开发初期使用；后续会根据实际测试和社区反馈，逐步评估更大结构与更多扩展能力的演进方向。

## 这次发布的重点

- 保持最小闭环：`init / apply / validate`
- 保持标准化模块入口：`INDEX.md`、`SPEC.md`、`CHANGELOG.md`
- 保持轻量扩展面：`profiles/`、`templates/`、`.openclaw_skill/`
- 保持 GitHub Actions 基础验证
- 保持中文主页 + 英文镜像的发布形式

## 为什么这版是 beta 冻结

- 核心已经收口到 `harness_core/`
- `init / apply / validate` 统一到同一套核心模型
- `INDEX.md`、`SPEC.md`、`validate` 的 marker 语义已经对齐
- 默认一致性模式保持 `soft`
- 扩展保持示例优先、项目本地实现，而不是 core-owned runtime
- 本地扩展示例已经补齐并可运行

## 验证命令

```bash
python tools/validate_module.py examples/hello_world --strict --profile python-service
python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service
python -m py_compile tools/init_module.py tools/apply_harness.py tools/validate_module.py
python examples/local_extension/harness/run_harness.py
```

## 发布说明

- 这是 `v1.0.1 beta` 的冻结发布。
- 回滚锚点：`v1.0.0`
- 适合小项目、小模块、开发初期使用。
- 后续扩展和更大结构会基于测试和反馈继续评估。
