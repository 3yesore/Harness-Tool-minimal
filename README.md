# Harness Tool - Minimal Edition

**轻量级 AI 模块维护工具 - 让 AI 安全接手任何模块**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/YOUR_USERNAME/harness-tool-minimal)

## 什么是 Harness Tool?

Harness Tool 是一套工程规范,通过标准化接口和清晰索引,让 AI 能够跨会话、跨模型安全接手模块维护。

**核心理念**: 不是让 AI 完全不依赖上下文,而是通过标准化降低依赖程度。

## 为什么需要 Harness?

传统开发中,AI 维护模块面临的问题:
- ❌ 每次都要重新理解整个代码库
- ❌ 缺少标准化接口,容易引入 bug
- ❌ 没有验证机制,改动风险高
- ❌ 换个 AI 或新会话就要重新开始

Harness 解决方案:
- ✅ INDEX.md 快速定位模块职责和关键文件
- ✅ SPEC.md 明确输入输出和错误处理
- ✅ 冒烟测试快速验证改动
- ✅ 任何 AI 都能通过索引快速上手

## 快速开始

### 1. 初始化新模块

```bash
python tools/init_module.py my_module --path modules
```

生成标准结构:
```
my_module/
├── INDEX.md          # 模块索引
├── SPEC.md           # 接口规范
├── CHANGELOG.md      # 变更历史
├── src/              # 源代码
├── tests/            # 测试
└── configs/          # 配置
```

### 2. 验证模块合规性

```bash
python tools/validate_module.py modules/my_module
```

### 3. 查看完整示例

```bash
cd examples/hello_world
python tests/smoke.py
```

## 核心特性

### 📋 标准化结构
- **INDEX.md**: 模块职责、关键文件、依赖关系
- **SPEC.md**: 输入输出、配置、错误处理
- **CHANGELOG.md**: 变更历史追踪

### 🔧 开箱即用工具
- **init_module.py**: 一键生成符合规范的模块骨架
- **validate_module.py**: 自动检查模块合规性
- **apply_harness.py**: 为现有模块半自动补 INDEX/SPEC/CHANGELOG 骨架

### 🩺 AI 修复能力
- **AI_REPAIR_GUIDE.md**: 给 AI 的标准修复路径
- 强调“先验证、再修复、再验证”
- 不依赖额外自动修复器

### ✅ 完整示例
- **hello_world**: 包含完整实现的参考模块

### 🔌 OpenClaw 集成
- 可作为 OpenClaw Skill 直接使用

## 模块结构说明

```
module_name/
├── INDEX.md           # 必需 - 模块索引
├── SPEC.md            # 必需 - 接口规范
├── CHANGELOG.md       # 推荐 - 变更历史
├── src/               # 源代码
├── tests/             # 测试(必需至少有冒烟测试)
├── configs/           # 配置文件
└── docs/              # 详细文档(可选)
```

## 使用场景

1. **新模块开发**: 从一开始就建立 AI 可维护的结构
2. **代码重构**: 让现有代码更容易被 AI 接手
3. **项目标准化**: 建立团队级维护规范
4. **遗留代码**: 为文档不清晰的模块补充索引

## AI 工作流

当 AI 维护 harness 模块时:

1. **定位** → 读取主 INDEX.md 找到目标模块
2. **理解** → 读取模块的 INDEX.md + SPEC.md (不读全部代码)
3. **选择性阅读** → 只读取任务相关的代码文件
4. **执行** → 按照 SPEC 约束进行修改
5. **验证** → 运行冒烟测试
6. **记录** → 更新 CHANGELOG.md

## 文档

- [核心规范](HARNESS_SPEC.md) - 完整的 Harness 工程规范
- [主索引](INDEX.md) - 仓库结构说明
- [示例模块](examples/hello_world/) - 完整参考实现
- [OpenClaw Skill](.openclaw_skill/SKILL.md) - OpenClaw 集成

## 版本规划

Harness Tool 提供三个版本:

| 版本 | 定位 | 核心功能 |
|------|------|----------|
| **Minimal** (本仓库) | 个人/小项目 | 核心规范 + 基础工具 |
| **Standard** | 中型项目 | + 项目级管理 + 多模块协调 |
| **Enterprise** | 大型/企业 | + CI/CD + 团队协作 + 审计 |

详见 [VERSION_ROADMAP.md](VERSION_ROADMAP.md)

## OpenClaw Skill 安装

```bash
# 复制到 OpenClaw skills 目录
cp -r .openclaw_skill ~/.openclaw/skills/harness

# 或 Windows
xcopy /E /I .openclaw_skill %USERPROFILE%\.openclaw\skills\harness
```

## 贡献

欢迎提交 Issue 和 PR!

## License

MIT License - 详见 [LICENSE](LICENSE)

## 相关项目

- [OpenClaw](https://github.com/openclaw/openclaw) - AI 助手框架
- Harness Tool Standard - 标准版 (规划中)
- Harness Tool Enterprise - 企业版 (规划中)
