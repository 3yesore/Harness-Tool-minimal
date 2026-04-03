# Harness Tool - Minimal

**让 AI 安全接手任何模块的维护工作**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/YOUR_USERNAME/harness-tool-minimal)
[![Validate](https://github.com/YOUR_USERNAME/harness-tool-minimal/workflows/Validate%20Examples/badge.svg)](https://github.com/YOUR_USERNAME/harness-tool-minimal/actions)

---

## 一句话

通过标准化的 **INDEX.md**（索引）和 **SPEC.md**（接口规范），让 AI 能够跨会话、跨模型安全维护你的代码模块。

---

## 核心问题

传统 AI 辅助开发的三大痛点：

❌ **每次都要重新理解整个项目** → 浪费时间和 token  
❌ **缺少标准化接口** → AI 容易引入 bug  
❌ **换个 AI 或新会话就要重新开始** → 无法持续维护

---

## Harness 解决方案

✅ **INDEX.md** → AI 快速定位模块职责和关键文件  
✅ **SPEC.md** → 明确输入输出和错误处理  
✅ **tests/smoke.py** → 验证改动正确性  
✅ **AI_CHECKLIST.md** → 标准化维护流程

**结果**：任何 AI 都能通过索引快速接手，无需依赖历史对话上下文。

---

## 10 秒快速开始

```bash
# 1. 初始化新模块
python tools/init_module.py my_module

# 2. 验证模块
python tools/validate_module.py my_module

# 3. 运行测试
cd my_module && python tests/smoke.py
```

---

## 真实示例

### 最小示例：hello_world
```bash
cd examples/hello_world
python tests/smoke.py
```

### 中等复杂度：user_service
用户注册认证服务，展示：
- 多文件组织
- 配置管理
- 完整错误处理
- 多场景测试

```bash
cd examples/user_service
python tests/smoke.py
```

---

## 核心特性

### 📋 标准化结构
- **INDEX.md**: 模块职责、关键文件、依赖关系
- **SPEC.md**: 输入输出、配置、错误处理
- **CHANGELOG.md**: 变更历史追踪

### 🔧 开箱即用工具
- **init_module.py**: 一键生成符合规范的模块骨架
- **validate_module.py**: 自动检查模块合规性
- **apply_harness.py**: 为现有模块半自动补 INDEX/SPEC 骨架

### 🩺 AI 自修复能力
- **AI_REPAIR_GUIDE.md**: 给 AI 的标准修复路径
- 强调"先验证、再修复、再验证"
- 不依赖额外自动修复器

### 🔌 OpenClaw 集成
- 可作为 OpenClaw Skill 直接使用
- 详见 `.openclaw_skill/SKILL.md`

---

## 适用场景

✅ 个人项目或小团队（< 10 模块）  
✅ Vibecoding 开发模式  
✅ 需要频繁切换 AI 模型或会话  
✅ 希望代码可被 AI 长期维护  
✅ 不想引入复杂依赖和工具链

---

## 设计哲学

> **不是让 AI 完全不依赖上下文，而是通过标准化降低依赖程度。**

Harness Tool 的核心理念：
- 通过**规范**赋能 AI，而非通过**自动化**代替 AI
- 保持**轻量**（零外部依赖，< 100KB）
- 强调**可验证**（测试必须通过）
- 支持**可交接**（任何 AI 都能接手）

---

## 文档

- [核心规范](HARNESS_SPEC.md) - 完整的 Harness 工程规范
- [AI 检查清单](AI_CHECKLIST.md) - AI 维护模块的标准流程
- [AI 修复指引](AI_REPAIR_GUIDE.md) - 验证失败时的修复路径
- [主索引](INDEX.md) - 仓库结构说明
- [FAQ](FAQ.md) - 常见问题解答

---

## 版本规划

| 版本 | 定位 | 核心功能 |
|------|------|----------|
| **Minimal** (当前) | 个人/小项目 | 核心规范 + 基础工具 |
| **Fetcher** | Codex/Claude 优化 | + 模型专属优化 + 高度自定义 |
| **Intruder** | 企业级 | + CI/CD + 团队协作 + 审计 |

详见 [VERSION_ROADMAP.md](VERSION_ROADMAP.md)

---

## 快速链接

- 📖 [开始使用](#10-秒快速开始)
- 🎯 [查看示例](#真实示例)
- 🤝 [贡献指南](CONTRIBUTING.md)
- ❓ [常见问题](FAQ.md)
- 📊 [GitHub Actions](.github/workflows/validate.yml)

---

## OpenClaw Skill 安装

```bash
# 复制到 OpenClaw skills 目录
cp -r .openclaw_skill ~/.openclaw/skills/harness

# 或 Windows
xcopy /E /I .openclaw_skill %USERPROFILE%\.openclaw\skills\harness
```

---

## 贡献

欢迎提交 Issue 和 PR！详见 [CONTRIBUTING.md](CONTRIBUTING.md)

---

## License

MIT License - 详见 [LICENSE](LICENSE)

---

## 相关项目

- [OpenClaw](https://github.com/openclaw/openclaw) - AI 助手框架
- Harness Tool Fetcher - Codex/Claude 优化版（规划中）
- Harness Tool Intruder - 企业版（规划中）

---

**让 AI 成为你的长期代码维护伙伴。**
