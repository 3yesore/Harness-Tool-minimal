# Harness Tool 设计复核

## 当前 `v1.0.1 beta` 的核心价值

1. 核心协议已经稳定在 `INDEX.md`、`SPEC.md`、smoke test 和 `validate` 这一条主合同路径上。
2. `init / apply / validate` 已统一回到同一套核心模型。
3. 示例模块可运行，并且能作为最小参考路径。
4. `templates/` 与 `profiles/` 已形成明确扩展面。
5. `v1.0.1 beta` 已经是独立冻结基线。

## 当前允许继续加强的方向

### 1. 文档与协议入口统一

- 统一中英文主入口
- 统一协议地图
- 统一 “contract-first + bridge-side” 的仓库定位

### 2. 版本基线与回滚锚点

- 明确 `v1.0.1 beta`
- 保留回滚锚点
- 区分核心基线与桥接验证

### 3. 收紧 validate 的表达，不扩 scope

- 保持文档章节校验准确
- 保持 smoke test 执行稳定
- 保持错误输出可读
- 不把 `validate` 做成厚分析平台

### 4. 保持 templates / profiles 的轻量边界

- 模板只提供安全默认值
- profile 只提供轻量预设
- 不把 profile 发展成 policy engine

### 5. 保持 `.openclaw_skill/` 同步

- 让 skill mirror 与主合同一致
- 避免 mirror 漂移出第二套语义

## 当前禁止继续扩张的方向

### 1. 把 kernel 做厚

- 不引入业务运行时到 kernel
- 不把 kernel 做成大平台

### 2. 过度源码分析

- 不把全仓库语义理解塞进核心
- 不把 AST / 深度分析做成默认路径

### 3. 默认自动修复

- 不把 validator 做成强修复器
- 不让默认路径隐式改动模块结构

### 4. 过厚规则系统

- 不把 profile 变成 policy engine
- 不引入复杂继承和冲突合并

### 5. 模板教程化

- 不把模板写成教学手册
- 不让模板承担解释整个系统的职责

### 6. 让 OpenHarness runtime 进入 core

- 不把 provider / middleware / session / runtime ownership 移进 `harness_core`
- OpenHarness 只保留 bridge-side 接入

## 性能底线

- 默认路径保持简短
- 脚手架保持明确
- 验证输出可读
- 不引入重型运行时依赖

## Harness 判断标准

- 合同明确
- 入口稳定
- 验证可跑
- 可交接
- 可扩展
- 边界清楚

## 结论

`v1.0.1 beta` 当前的方向仍然正确：强调 hard contract、thin core、large extension surface，并把 OpenHarness 兼容性保持在外层 bridge / binding 路径，不改变 `harness_tool` 的上游定位。
