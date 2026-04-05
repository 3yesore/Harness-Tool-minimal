# v1.0.1 beta 版本说明

## 版本名称

- `Harness Tool Minimal v1.0.1 beta`

## 一句话说明

- 这是一次围绕 minimal 基线做的 beta 发布，重点不是扩张功能，而是把最小闭环做稳、把标准入口做清楚、把扩展边界做明确。

## 核心变化

- 继续保持 `init / apply / validate` 的最小闭环，确保模块接入、校验和交接流程一致。
- 继续保留 `INDEX.md`、`SPEC.md`、`CHANGELOG.md` 和 `tests/smoke.py` 这套最小可交接结构。
- `profiles/`、`templates/` 和 `.openclaw_skill/` 继续作为轻量扩展面，而不是厚重平台。
- GitHub Actions 继续承担基础自动校验职责，保证仓库状态可验证。
- 中文主页和英文镜像继续并存，适合发布和分发。

## 对外承诺

- 这版最适合小项目、小模块、开发初期使用。
- 它提供的是最小但完整的 Harness 工作流，不是大而全的平台。
- 用户可以在现有结构上继续做项目级自定义，但仍然遵守最小合同。
- 后续如果需要更大结构或更多自动化能力，会在实际测试和反馈基础上逐步推进。

## 验证结果

以下命令已经在仓库中通过验证：

- `python tools/validate_module.py examples/hello_world --strict --profile python-service`
- `python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service`
- `python -m py_compile tools/init_module.py tools/apply_harness.py tools/validate_module.py`

## 风险说明

- 当前版本的扩展面仍然是轻量型的，适合项目级约定，不是统一运行时平台。
- 版本仍然遵循 minimal 原则，所以不会把核心做厚。
- 如果项目规模较大，建议结合 `profiles/`、`templates/` 和现有示例逐步定制，不要期待这一版就覆盖所有大型工程场景。

## 回滚锚点

- `v1.0.0`

## 准确性确认

下面这些事实已经在仓库里验证过，可以安全写进版本说明：

- 仓库当前核心能力包括初始化模块、为现有模块补 Harness、以及验证模块文档和冒烟测试。
- `examples/hello_world` 和 `examples/user_service` 都是当前仓库中的参考示例。
- `profiles/`、`templates/` 和 `.openclaw_skill/` 确实存在，并且是当前扩展和分发的主要入口。
- 默认使用 `v1.0.0` 作为历史锚点，`v1.0.1 beta` 作为当前 beta 冻结版本。

## 建议发布口径

- 本次更新简而言之是一些基线加固工作和开放了一些标准化拓展，并且都是在 minimal 基础上做的稳定性建设。但目前仍建议在小项目小模块的开发初期使用。具体更新内容请移步（[VERSION_DESCRIPTION.zh.md](VERSION_DESCRIPTION.zh.md)），后续会根据我实际测试推出更多的扩展和大结构更新，届时会根据社区反响尝试往大型项目的方向推进，敬请期待，欢迎讨论！

