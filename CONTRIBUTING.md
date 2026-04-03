# Contributing to Harness Tool

感谢你对 Harness Tool 的关注！

## 贡献方式

### 报告问题
- 使用 GitHub Issues 报告 bug
- 提供复现步骤和环境信息
- 如果可能，提供最小复现示例

### 提交改进
1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交变更 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启 Pull Request

## 开发规范

### 代码风格
- Python: 遵循 PEP 8
- 文档: 使用 Markdown
- 提交信息: 使用清晰的英文描述

### 测试要求
- 所有新功能必须有测试
- 运行 `python tools/validate_module.py` 确保合规
- 示例模块必须通过冒烟测试

### 文档要求
- 新功能必须更新相关文档
- 保持 README.md 简洁
- 详细说明放在对应的 .md 文件

## Harness 规范本身的贡献

如果你想改进 Harness 规范：

1. **提出讨论**: 先在 Issue 中讨论变更必要性
2. **向后兼容**: 新规范必须兼容现有模块
3. **更新示例**: 同步更新 hello_world 和 user_service
4. **版本标注**: 在 HARNESS_SPEC.md 中标注版本变更

## 不接受的贡献

- 引入重度外部依赖（Minimal 版保持零依赖）
- 复杂的自动化工具（与 Minimal 理念冲突）
- 未经讨论的规范破坏性变更

## 行为准则

- 尊重他人
- 建设性讨论
- 专注技术本身

## 许可

贡献的代码将采用 MIT 许可证。
