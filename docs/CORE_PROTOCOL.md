# Harness Tool Core Protocol

## 作用
`core` 只负责最小且必须冻结的合同，不负责外部接入运行时。

## 冻结对象
- `ModuleContext`
- `ContractRules`
- `ValidationResult`
- `ScaffoldPlan`

## 冻结阶段
- `Discovery`
- `Contract`
- `Validate`
- `Suggest`

## core 必须硬的东西
- 合同字段
- 工作流阶段
- 结果格式
- 生成计划
- 最低验证门槛

## core 不做的事
- 不接 OS 运行时
- 不接多 agent 调度
- 不接外部项目翻译
- 不承载项目本地业务语义
- 不做厚平台

## 默认原则
- 核心薄
- 合同硬
- 扩展显式
- 默认路径简单
- 高级接入走外层适配
