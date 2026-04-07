# harness_core 快速规范入口摘要

如果你只读一页，就读这一页。

## 先记住 3 句
- `harness_core` 只放薄核心，不放 CLI 细节和业务逻辑。
- `INDEX.md` 讲模块有什么、哪里重要。
- `SPEC.md` 讲模块怎么被调用、怎么被验证。

## 4 个子模块的职责
- `__init__.py`：稳定导出和公共 API 入口
- `core.py`：数据模型、计划生成、验证编排
- `rendering.py`：模板和 marker 文本渲染
- `markers.py`：关键路径、关键变量、关键耦合的显式说明

## marker 规则
- `INDEX.md` 写模块内关键路径、关键状态、关键耦合。
- `SPEC.md` 额外写 `call_path`、`call_entry`、`entry_file`。
- `validate` 会检查 marker 是否存在、是否指向真实文件、是否彼此一致。

## 边界规则
- `core.py` 可以调用 `rendering.py`。
- `rendering.py` 不能反向依赖 `core.py`。
- `markers.py` 只描述，不执行业务。
- `tools/` 和 `.openclaw_skill/scripts/` 只做薄入口。

## 扩展规则
- `profiles/` 只扩展预设规则。
- `templates/` 只扩展默认骨架。
- `override` 只改项目本地默认值，不能破坏 contract。

## 程序入口
- `harness_core.describe_core_boundaries()`
- `harness_core.describe_development_guidance()`
- `harness_core.describe_extension_guidance()`
- `harness_core.describe_marker_registry()`

