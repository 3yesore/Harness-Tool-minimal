# Harness Tool 1.0.1 发布包

[English](README.en.md) | [中文](README.md)

这是 `Harness Tool 1.0.1` 的发布准备包主页。

## 这个包的作用

- 汇总当前版本对外发布需要带走的文案
- 作为发布前检查的统一入口
- 作为发布后回看的版本资料入口

## 当前发布结论

当前版本已经适合作为你自己的项目基线发布。

对外应统一表述为：

- `harness_tool` 是上游、contract-first 基底
- `harness_core` 保持薄，不宿主 runtime
- OpenHarness 兼容能力停留在 bridge / binding 外层
- 外部验证已完成，但它代表兼容性证据，不代表 runtime ownership

## 包内主要文件

- [VERSION_DESCRIPTION.zh.md](VERSION_DESCRIPTION.zh.md)
- [VERSION_DESCRIPTION.en.md](VERSION_DESCRIPTION.en.md)
- [GITHUB_RELEASE.zh.md](GITHUB_RELEASE.zh.md)
- [GITHUB_RELEASE.en.md](GITHUB_RELEASE.en.md)
- [PUBLISH_CHECKLIST.zh.md](PUBLISH_CHECKLIST.zh.md)
- [PUBLISH_CHECKLIST.en.md](PUBLISH_CHECKLIST.en.md)
- [MANIFEST.md](MANIFEST.md)

## 当前版本边界

这个发布包明确支持：

- 薄核心、强合同的仓库叙事
- 模板、规则、示例和 skill mirror 的冻结基线
- OpenHarness-compatible bridge 与 repo-external 验证

这个发布包不声称：

- 已完整接入 OpenHarness runtime
- 已完成 provider / middleware live wiring
- 已完成 session / conversation integration

## 建议发布策略

- 先完成仓库内的 freeze groups 提交
- 再以 `Harness Tool 1.0.1` 对外发布
- 发布后如果要给 OpenHarness 上游贡献，优先贡献：
  - docs
  - example
  - compatibility note

## 发布状态建议

- 当前状态：可发布的稳定基线
- 发布策略：冻结基线，不继续厚化 core
- 后续策略：只接受 bug 修复、文档修正、兼容性补丁和经过验证的边界收紧
