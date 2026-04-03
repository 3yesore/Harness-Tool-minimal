# Harness Tool v1.0 - Minimal Edition

**让 AI 安全接手任何模块的维护工作**

---

## 🎉 首次发布

Harness Tool Minimal v1.0 是一套轻量级工程规范，通过标准化的 INDEX.md（索引）和 SPEC.md（接口规范），让 AI 能够跨会话、跨模型安全维护你的代码模块。

---

## ✨ 核心特性

### 📋 标准化结构
- **INDEX.md**: 模块职责、关键文件、依赖关系
- **SPEC.md**: 输入输出、配置、错误处理
- **CHANGELOG.md**: 变更历史追踪
- **tests/smoke.py**: 快速验证

### 🔧 开箱即用工具
- `init_module.py`: 一键生成符合规范的模块骨架
- `validate_module.py`: 自动检查模块合规性
- `apply_harness.py`: 为现有模块半自动补 INDEX/SPEC 骨架

### 🩺 AI 友好设计
- `AI_CHECKLIST.md`: AI 维护模块的标准流程
- `AI_REPAIR_GUIDE.md`: 验证失败时的修复路径
- `AI_OPERATIONS.md`: 结构化操作指令（XML 标签）

### 🔌 OpenClaw 集成
- 可作为 OpenClaw Skill 直接使用
- 详见 `.openclaw_skill/SKILL.md`

---

## 📦 包含内容

### 核心文档
- `HARNESS_SPEC.md` - 完整的 Harness 工程规范
- `README.md` - 项目说明和快速开始
- `INDEX.md` - 仓库结构索引
- `VERSION_ROADMAP.md` - 版本规划（Minimal/Fetcher/Intruder）

### AI 指引
- `AI_CHECKLIST.md` - AI 维护检查清单
- `AI_REPAIR_GUIDE.md` - AI 修复指引
- `AI_OPERATIONS.md` - 结构化操作手册

### 工具脚本
- `tools/init_module.py` - 初始化新模块
- `tools/validate_module.py` - 验证模块合规性
- `tools/apply_harness.py` - 应用 harness 到现有模块

### 示例模块
- `examples/hello_world/` - 最小示例
- `examples/user_service/` - 中等复杂度示例（用户认证服务）

### 扩展支持
- `profiles/` - 规则配置系统（预留扩展点）
- `templates/` - INDEX/SPEC/CHANGELOG 模板

### 社区文档
- `CONTRIBUTING.md` - 贡献指南
- `FAQ.md` - 常见问题解答
- `LICENSE` - MIT 许可证

### CI/CD
- `.github/workflows/validate.yml` - GitHub Actions 自动验证

---

## 🚀 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/YOUR_USERNAME/harness-tool-minimal.git
cd harness-tool-minimal

# 2. 初始化新模块
python tools/init_module.py my_module

# 3. 验证模块
python tools/validate_module.py my_module

# 4. 运行测试
cd my_module && python tests/smoke.py
```

---

## 📊 统计数据

- **文件数量**: 50
- **总大小**: ~117 KB
- **代码行数**: ~3000 行
- **外部依赖**: 0
- **示例模块**: 2 个
- **测试覆盖**: 100%

---

## 🎯 适用场景

✅ 个人项目或小团队（< 10 模块）  
✅ Vibecoding 开发模式  
✅ 需要频繁切换 AI 模型或会话  
✅ 希望代码可被 AI 长期维护  
✅ 不想引入复杂依赖和工具链

---

## 🔄 版本规划

| 版本 | 定位 | 状态 |
|------|------|------|
| **Minimal** | 个人/小项目 | ✅ v1.0 已发布 |
| **Fetcher** | Codex/Claude 优化 | 🔜 规划中 |
| **Intruder** | 企业级 | 🔜 规划中 |

---

## 📚 文档

- [核心规范](HARNESS_SPEC.md)
- [AI 检查清单](AI_CHECKLIST.md)
- [AI 修复指引](AI_REPAIR_GUIDE.md)
- [FAQ](FAQ.md)
- [贡献指南](CONTRIBUTING.md)

---

## 🤝 贡献

欢迎提交 Issue 和 PR！详见 [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE)

---

## 🔗 相关项目

- [OpenClaw](https://github.com/openclaw/openclaw) - AI 助手框架
- Harness Tool Fetcher - Codex/Claude 优化版（规划中）
- Harness Tool Intruder - 企业版（规划中）

---

## 💬 社区

- GitHub Discussions
- [OpenClaw Discord](https://discord.com/invite/clawd)

---

**让 AI 成为你的长期代码维护伙伴。**
