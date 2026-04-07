# v1.0.1 beta 版本说明

## 版本名称

- `Harness Tool Minimal v1.0.1 beta`

## 一句话说明

- 这是一次面向发布的冻结版本：核心继续保持薄、合同继续保持硬，并在不污染 `core` 的前提下补齐了 OpenHarness-compatible bridge 与外部验证链。

## 版本定位

- `harness_tool` 仍然是上游、contract-first 基底
- `harness_core` 仍然只负责协议、验证、阶段和 scaffold 语义
- OpenHarness 相关能力仍然停留在 bridge / binding 外层
- 外部验证是兼容性证据，不是 runtime ownership

## 核心变化

### 1. Core / contract 基线冻结

- 顶层入口文档已经统一到同一套协议叙事：
  - `README.md`
  - `INDEX.md`
  - `HARNESS_SPEC.md`
- `CORE_PROTOCOL.md`、`ADAPTER_PROTOCOL.md`、`EXTENSION_PROTOCOL.md` 已明确三层边界
- `harness_core/` 已作为统一合同层存在，不再依赖分散脚本语义
- `init / apply / validate` 继续通过同一套核心模型协作

### 2. 模板、规则与示例对齐

- `templates/` 已与当前合同标题和字段一致
- `profiles/` 仍然保持轻量，只描述默认规则预设
- `examples/hello_world/` 继续作为最小合同示例
- `examples/local_extension/` 保留项目本地扩展示例

### 3. OpenClaw skill mirror 对齐

- `.openclaw_skill/` 继续作为 mirror，而不是独立产品面
- mirror 的模板、规则、脚本与当前主合同已经对齐一层

### 4. OpenHarness-compatible bridge 补齐

- 增加了窄桥式的 OpenHarness bridge / binding 能力：
  - `OPENHARNESS_BRIDGE.md`
  - `OPENHARNESS_SDK_BINDING.md`
  - `OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.md`
- `adapters/` 和 `scripts/openharness_*` 只负责桥接，不进入 `harness_core`
- `provider_hints` / `middleware_hints` 仍然只是 bridge metadata，不是 core semantics

### 5. 外部验证完成

- 仓库内已有 `examples/openharness_app/` 作为最小 OpenHarness app 示例
- 仓库外已有真实验证目录：
  - `C:/Users/Y2516/Desktop/openharness_app_external_verify`
- 已验证：
  - `Agent` 实例化
  - `Agent.run(...)` mock dry-run
  - `harness_validate` process transport

## 对外承诺

- 这个版本可以作为你自己的 `harness_tool` 基线发布
- 它提供的是：
  - 薄核心
  - 强合同
  - 明确扩展边界
  - 可验证的 OpenHarness-compatible bridge
- 它不提供的是：
  - core-owned runtime
  - provider lifecycle 托管
  - middleware lifecycle 托管
  - session / conversation 深集成

## 当前验证结果

以下检查已在当前仓库和外部验证目录跑通：

- `python tools/validate_module.py examples/hello_world --strict --profile python-service`
- `python tools/validate_module.py examples/local_extension --strict --profile default`
- `python tools/validate_module.py examples/openharness_app --strict --profile default`
- `python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service`
- `npm run build` in `C:/Users/Y2516/Desktop/openharness_app_external_verify`
- `npm run smoke` in `C:/Users/Y2516/Desktop/openharness_app_external_verify`

## 风险说明

- 当前 OpenHarness 集成仍然是窄桥，不是完整 runtime 集成
- 仍未纳入：
  - live provider wiring
  - live middleware wiring
  - non-process transport
  - session / conversation validation
  - real model invocation
- 这不是问题隐藏，而是刻意保留在 bridge open items 中，避免污染 `core`

## 适用范围

- 适合发布为你自己的仓库基线版本
- 适合小项目、小模块、以及需要先做硬合同的工程起点
- 适合继续作为上游基底扩展更多 bridge / compatibility 路径
- 不适合被表述成“已完整接入 OpenHarness runtime”

## 回滚锚点

- `v1.0.0`

## 建议发布口径

- `Harness Tool Minimal v1.0.1 beta` 是一个以冻结和收口为主的版本，不追求平台化扩张
- 当前版本已经具备：
  - 上游 contract-first 基底
  - 稳定的 core/extension 边界
  - OpenHarness-compatible bridge
  - 外部验证证据
- 后续贡献到 OpenHarness 上游时，更适合拆成 docs / example / compatibility note，而不是直接推整套接口层
