# Harness Tool Extension Protocol

## 作用
`extension` 是项目本地变化层，负责在不破坏 core 的前提下调预设、改骨架、标关键点、做局部覆盖。

## 四个扩展面
- `profiles`
- `templates`
- `marker`
- `override`

## 允许软化的内容
- `profiles` 的默认值和预设组合
- `templates` 的文案和布局
- `marker` 的描述方式和辅助信息
- `override` 的目录偏好和 wrapper 习惯

## 不能碰的底线
- 不能破坏 core contract
- 不能绕过 validate
- 不能修改协议字段语义
- 不能把扩展伪装成 core

## 推荐原则
- 默认保持 `soft`
- 必需项和推荐项分开
- 项目本地差异留在项目仓库
- 需要更复杂行为时，先做示例，再决定是否回流主线

## extension 的目标
- 让自定义容易接入
- 让扩展不散架
- 让 core 不变厚
