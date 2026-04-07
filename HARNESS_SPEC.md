# Harness 规范 v1.0.1 beta

## 目标

`Harness Tool Minimal` 不是厚平台，而是一个面向模块开发与维护全生命周期的 `harness kernel`。它的目标是把职责、接口、验证和交接信息收拢到少量固定文件里，让人和 AI 在开发、接入、演进和维护阶段都能保持一致。

## 四层边界

### 1. Core
`core` 只负责机制，不承载项目业务语义。

`core` 应冻结：
- `ModuleContext`
- `ContractRules`
- `ValidationResult`
- `ScaffoldPlan`
- `Discovery -> Contract -> Validate -> Suggest`

`core` 不负责：
- OS 运行时接入
- 多 agent 调度
- 外部项目翻译
- 厚平台逻辑

### 2. Adapter
`adapter` 是 `core` 外层的接入翻译层。

`adapter` 应冻结：
- `name`
- `version`
- `type`
- `scope`
- `entrypoint`
- `capabilities`
- `protocol_version`
- `required_core_version`

`adapter` 应支持：
- `discover()`
- `attach()`
- `adapt()`
- `execute()`
- `teardown()`

`adapter` 输出：
- `adapted_context`
- `capability_report`
- `warnings`
- `errors`

`adapter` 不负责：
- 不裁判模块是否合格
- 不替代 `core contract`
- 不吞掉 `extension` 协议
- 不把自己做成厚平台

### 3. Extension
`extension` 负责项目本地差异，但不能破坏合同。

`extension` 包含：
- `profiles`
- `templates`
- `marker`
- `override`

`extension` 允许软化：
- 默认值
- 文案
- 预设
- 本地 wrapper
- 目录偏好

`extension` 不允许：
- 绕过 `validate`
- 改变协议字段语义
- 破坏 `core contract`
- 伪装成 `core`

### 4. Override
`override` 只允许项目本地覆盖默认选择，不允许突破底线。

## 工作流阶段

冻结四段工作流：
- `Discovery`
- `Contract`
- `Validate`
- `Suggest`

说明：
- `Discovery` 发现仓库与模块结构
- `Contract` 验证合同、marker、入口一致性
- `Validate` 执行冒烟测试、配置检查和推荐项检查
- `Suggest` 输出缺口、扩展建议和补丁草案

## 合同最小形状

一个模块至少应具备：
- `INDEX.md`
- `SPEC.md`
- `tests/smoke.py`
- `CHANGELOG.md`

建议项：
- `configs/default.json`
- `src/main.py`
- 额外 marker 说明

## 协议地图

仓库级规范入口应保持一致：
- 文档入口：[`harness_core/BOUNDARIES.md`](harness_core/BOUNDARIES.md)
- 扩展入口：[`harness_core/EXTENSIONS.md`](harness_core/EXTENSIONS.md)
- 协议文件：
  - [`CORE_PROTOCOL.md`](CORE_PROTOCOL.md)
  - [`ADAPTER_PROTOCOL.md`](ADAPTER_PROTOCOL.md)
  - [`EXTENSION_PROTOCOL.md`](EXTENSION_PROTOCOL.md)

## 最低验证门槛

### 必须检查
- 必需文件存在
- 必需章节存在
- 入口存在
- marker 核心项存在
- smoke test 可执行
- 配置文件可解析

### 软提示
- marker 的具体写法
- template 的布局偏好
- profile 的默认值
- 本地 wrapper 的组织方式
- 项目目录偏好

## 仍未收口的事项

以下事项当前先保留为说明和样例，不直接并入 `core`：
- `adapters/` 下的具体适配器样例
- OS / 多 agent / 外部项目接入演示
- 更细的 adapter 校验矩阵
- 更完整的扩展包版本化方案

## 版本原则

- `v1.0.1 beta` 是独立冻结基线
- 旧版本仅作为历史参考
- 后续扩展必须遵守当前版本 contract
- 默认保持 `soft`，但软约束必须建立在冻结协议之上

## OpenHarness 外部复核状态

当前 bridge / SDK binding 已在仓库外部 OpenHarness app 目录复核通过：

- `Agent` 实例化通过
- `Agent.run(...)` 本地 mock 干跑通过
- `harness_validate` process transport 调用通过
- `provider_hints` / `middleware_hints` 仍为 bridge contract，不进入 `core`
