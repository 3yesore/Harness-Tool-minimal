# Harness Tool Minimal v1.0.1 历史基线

`v1.0.1 beta` 代表这套 minimal 基线的冻结版本。  
它已经不是一个继续向平台化扩张的试验版，而是一个可以作为历史基线长期参考的展示页版本。

如果你要看完整的版本说明、风险边界和资源包内容，请移步：[VERSION_DESCRIPTION.zh.md](VERSION_DESCRIPTION.zh.md)。  
如果你想直接看这版的历史基线展示，请移步：[DISPLAY_PAGE.zh.md](DISPLAY_PAGE.zh.md)。

## 这版展示什么

- 最小闭环：`init / apply / validate`
- 标准化模块入口：`INDEX.md`、`SPEC.md`、`CHANGELOG.md`
- 轻量扩展面：`profiles/`、`templates/`、`.openclaw_skill/`
- 默认一致性模式：`soft`
- 扩展方式：示例优先、项目本地实现

## 为什么它值得保留

- 它把模块开发、验证、交接和记录收束到少量固定文件中。
- 它保留了项目级自定义空间，同时不让 core 变厚。
- 它适合小项目、小模块、开发初期的持续使用。
- 它是后续扩展、实验和回流的历史基线。

## 验证命令

```bash
python tools/validate_module.py examples/hello_world --strict --profile python-service
python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service
python -m py_compile tools/init_module.py tools/apply_harness.py tools/validate_module.py
python examples/local_extension/harness/run_harness.py
```

## 发布说明

- 回滚锚点：`v1.0.0`
- 本页定位：历史基线展示页
- 推荐使用方式：作为后续实验和扩展回流的参考基线
