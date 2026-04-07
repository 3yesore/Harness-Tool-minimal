# 工作索引

这个索引不是最终冻结结果，而是当前仓库的整理入口。它告诉后续收尾时，哪些内容应该先冻结，哪些内容应该继续保留为开放项。

## 当前优先级

### 第一层：Core 已冻结
优先保留并按最终协议整理：
- `CORE_PROTOCOL.md`
- `ADAPTER_PROTOCOL.md`
- `EXTENSION_PROTOCOL.md`
- `harness_core/`
- `tools/`

### 第二层：主入口文档
这些文档必须和协议地图保持同一叙事：
- `README.md`
- `README.en.md`
- `INDEX.md`
- `INDEX.en.md`
- `HARNESS_SPEC.md`
- `HARNESS_SPEC.en.md`
- `VERSION_ROADMAP.md`
- `VERSION_ROADMAP.en.md`
- `DESIGN_REVIEW.md`
- `AI_CHECKLIST.md`
- `GITHUB_RELEASE.md`

### 第三层：扩展面
这些内容要保持可见，但不要在本轮继续厚化：
- `profiles/`
- `templates/`
- `adapters/`
- `examples/local_extension/`
- `.openclaw_skill/`

### 第四层：开放项
这些内容先保留为文档和样例，不并入 `core`：
- `docs/OPEN_ITEMS.md`
- `docs/OPEN_ITEMS.en.md`
- `docs/CURRENT_CHANGESET_INDEX.md`
- `docs/CURRENT_CHANGESET_INDEX.en.md`
- `docs/FREEZE_GROUPS.md`
- `docs/FREEZE_GROUPS.en.md`
- `adapters/sample_usage.md`
- `adapters/workspace.py`
- 后续新增但尚未冻结的 adapter 样例

## 建议整理顺序

1. 先整理 `core` 协议文件和 `harness_core/`
2. 再整理主入口文档
3. 再整理 `adapters/` 样例和说明
4. 再整理 `profiles/`、`templates/`、`examples/`
5. 最后再检查 `.openclaw_skill/` 是否还需要镜像更新

## 冻结执行入口

- 责任分层入口：`docs/CURRENT_CHANGESET_INDEX.md`
- 提交批次入口：`docs/FREEZE_GROUPS.md`

## 保留原则

- 未完成事项继续保留在 `docs/OPEN_ITEMS.md`
- 做最终收尾时，先看 `docs/CURRENT_CHANGESET_INDEX.md`
- 做最终提交分组时，按 `docs/FREEZE_GROUPS.md` 执行
- 样例优先保留在 `adapters/` 或 `examples/`
- 不要把开放项提前并入 `core`
- 不要为了整理而把扩展空间收窄

## OpenHarness 路径

- `OPENHARNESS_BRIDGE.md`
- `OPENHARNESS_PROVIDER_MIDDLEWARE_CONTRACT.md`
- `OPENHARNESS_SDK_BINDING.md`
- `docs/OPENHARNESS_BRIDGE_OPEN_ITEMS.md`
- `docs/OPENHARNESS_BRIDGE_INDEX.md`
- `docs/OPENHARNESS_PROVIDER_MIDDLEWARE_OPEN_ITEMS.md`
- `docs/OPENHARNESS_PROVIDER_MIDDLEWARE_INDEX.md`
- `examples/openharness_app/`
- `docs/OPENHARNESS_APP_OPEN_ITEMS.md`
- `docs/OPENHARNESS_APP_INDEX.md`

## 使用方式

- 先看优先级
- 再按整理顺序处理
- 如果某项仍不确定，先留在开放项
- 只有真正冻结成协议的一部分，才从开放项移出
