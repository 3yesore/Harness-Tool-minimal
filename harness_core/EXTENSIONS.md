# harness_core 扩展入口摘要

这页只讲一件事：扩展要怎么接，才不会把核心做散。

## 先记住 3 句
- 核心只冻结骨架，不冻结项目业务。
- 更细的控制优先走 `profile`、`template`、`marker`、`override`。
- 扩展要显式、可解释、可替换，但不能越过 contract。

## 扩展层怎么分
- `profiles/`：调预设规则，不改底线。
- `templates/`：调默认长相，不改合同。
- `markers`：标关键点，不替代验证。
- `override`：做项目本地覆盖，不破坏边界。

## 推荐使用方式
- 默认保持 `soft` 约束。
- 需要更严格时，用 profile 显式收紧。
- 项目本地规则尽量写在项目仓库里，而不是塞进 `core.py`。
- 扩展如果需要更复杂的行为，先做示例，再考虑是否值得回流主线。

## 不建议做的事
- 不要把扩展挂载做成 core 内置运行时。
- 不要把所有项目差异都硬编码进核心。
- 不要让 template 或 profile 变成厚重策略系统。
- 不要让 override 绕开 `INDEX.md`、`SPEC.md` 和 `validate`。

## 程序入口
- `harness_core.describe_extension_guidance()`
- `harness_core.describe_core_boundaries()`
- `harness_core.describe_marker_registry()`

