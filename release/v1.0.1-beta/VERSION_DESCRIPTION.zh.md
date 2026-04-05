# v1.0.1 beta 版本说明

## 版本定位

`Harness Tool Minimal v1.0.1 beta` 是一次围绕 minimal 基线做的冻结发布。  
它的重点不是把工具做厚，而是把最小闭环、合同边界、验证口径和扩展入口进一步收紧并固化，使仓库可以作为长期可维护的开发框架底座继续使用。

## 版本名称

- `Harness Tool Minimal v1.0.1 beta`

## 一句话说明

- 这是一次基线加固型 beta 发布：核心更薄、合同更硬、扩展入口更清楚，同时保留足够大的项目级自定义空间。

## 核心变化

- `init / apply / validate` 继续统一到同一套核心模型，避免入口脚本各自维护不同逻辑。
- `harness_core/` 已成为共享底座，承担 `ContractRules`、`ModuleContext`、`ValidationResult`、`ScaffoldPlan` 等核心类型和编排逻辑。
- `INDEX.md`、`SPEC.md`、`validate` 的 marker 语义已经对齐，关键路径、入口和耦合点可以被快速识别。
- 默认一致性模式保持 `soft`，把收口限定在原则层面，不把不同项目的入口结构锁死。
- `profiles/`、`templates/` 与 `.openclaw_skill/` 仍然只承担轻量预设、默认骨架和分发镜像职责，不向 core 里收拢成厚重平台。
- 本地扩展示例已经补齐，说明项目可以自己在本地挂接扩展，而不是依赖 core 内置的扩展运行时。

## 对外承诺

- 适合小项目、小模块、开发初期场景。
- 适合从一开始就按 Harness 方式组织模块、规范和验证。
- 适合需要 AI 参与维护、但又希望上下文可恢复、可交接的工程流程。
- 不承诺把所有大型项目场景一次性覆盖完；更大的结构和更多自动化能力会基于实际测试和反馈逐步评估。

## 验证结果

以下命令在仓库中通过验证：

- `python tools/validate_module.py examples/hello_world --strict --profile python-service`
- `python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service`
- `python -m py_compile tools/init_module.py tools/apply_harness.py tools/validate_module.py`
- `python examples/local_extension/harness/run_harness.py`

## 风险说明

- 当前版本的扩展挂载是“示例优先、项目本地实现”的路线，不是统一运行时平台。
- 默认 marker / 入口一致性采用 `soft` 模式，灵活性保留了，但项目侧仍需要维护本地约定。
- 为保持 minimal，core 不会继续往平台化方向堆 mode 和旋钮，因此更细的控制应通过项目本地扩展实现。
- 如果项目已经是较大规模、多入口、多团队协作的工程，建议把这版作为基础层，而不是把它当作完整的平台替代品。

## 回滚锚点

- `v1.0.0`

## 准确性确认

下面这些事实已经在仓库里验证过，可以安全写进版本说明：

- 核心已经收口到 `harness_core/`，`init / apply / validate` 共享同一套核心模型。
- `INDEX.md`、`SPEC.md`、`validate` 的 marker 口径已经对齐。
- 默认一致性模式仍然是 `soft`，不会把项目自定义空间锁死。
- 本地扩展示例已经补齐，并且 `run_harness.py` 可以直接运行。
- 扩展挂载保持为示例优先和项目本地实现，不由 core 托管完整运行时。
- `v1.0.1 beta` 是独立的冻结基线，不与上一版本口径混用。

## 建议发布口径

- 本次更新是一次面向 minimal 基线的加固型 beta 发布，重点放在稳定性、交接性与标准化入口。
- 当前仍然更适合小项目、小模块、开发初期使用。
- 具体更新内容请结合 release 正文和版本说明查看；后续会根据实际测试和社区反馈，再决定是否向更大结构和更多扩展能力演进。
