# Harness Tool - Minimal

**基于 Harness Engineering 的模块化工程规范工具**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/3yesore/Harness-Tool-minimal)
[![Validate](https://github.com/3yesore/Harness-Tool-minimal/workflows/Validate%20Examples/badge.svg)](https://github.com/3yesore/Harness-Tool-minimal/actions)

---

## 什么是 Harness Engineering?

Harness Engineering 是一套模块化工程方法论，通过**标准化索引**（INDEX.md）和**接口规范**（SPEC.md），让模块具备：

- **可发现性**：通过索引快速定位模块职责和关键文件
- **可理解性**：通过规范明确输入输出和错误处理
- **可验证性**：通过测试确保模块正确性
- **可交接性**：支持跨会话、跨工具、跨人员的稳定维护

---

## 核心价值

### 1. 降低认知负担
不需要理解整个代码库，只需：
- 读取 INDEX.md 了解模块职责
- 读取 SPEC.md 了解接口约束
- 按需阅读相关代码文件

### 2. 标准化接口
- 输入输出格式明确
- 错误处理统一
- 配置与代码分离

### 3. 强制验证
- 每个模块必须有冒烟测试
- 修改后必须通过验证
- 明确的成功/失败标准

### 4. 持续可维护
- 变更历史可追溯（CHANGELOG.md）
- 接口变更有记录
- 支持长期演进

---

## 快速开始

### 初始化新模块

```bash
python tools/init_module.py my_module
```

生成标准结构：
```
my_module/
├── INDEX.md          # 模块索引
├── SPEC.md           # 接口规范
├── CHANGELOG.md      # 变更历史
├── src/              # 源代码
├── tests/            # 测试
└── configs/          # 配置
```

### 验证模块合规性

```bash
python tools/validate_module.py my_module
```

### 查看示例

```bash
# 最小示例
cd examples/hello_world && python tests/smoke.py

# 中等复杂度示例（用户认证服务）
cd examples/user_service && python tests/smoke.py
```

---

## 核心组件

### 📋 标准化文档
- **INDEX.md**: 模块职责、关键文件、依赖关系
- **SPEC.md**: 输入输出、配置、错误处理
- **CHANGELOG.md**: 变更历史追踪

### 🔧 工具链
- **init_module.py**: 初始化符合规范的模块骨架
- **validate_module.py**: 检查模块合规性
- **apply_harness.py**: 为现有模块补充 Harness 文档

### 📚 完整示例
- **hello_world**: 最小示例
- **user_service**: 中等复杂度示例（多文件、配置管理、错误处理）

### 🔌 扩展支持
- **profiles/**: 规则配置系统（支持自定义规范）
- **OpenClaw Skill**: 可作为 OpenClaw 技能直接使用

---

## 设计原则

### 索引优先 (Index-First)
通过 INDEX.md 快速定位，而非全量扫描代码。

### 规范化接口 (Standardized Interface)
输入输出标准化，降低理解成本和出错风险。

### 最小上下文 (Minimal Context)
关键信息集中在索引和规范，代码按需阅读。

### 可验证 (Verifiable)
每个模块必须有测试，修改后必须验证。

### 可交接 (Handoff-Ready)
支持跨会话、跨工具、跨人员的稳定维护。

---

## 适用场景

✅ **模块化开发**：为每个模块建立清晰的边界和接口  
✅ **团队协作**：统一的文档规范降低沟通成本  
✅ **长期维护**：变更历史和接口规范支持持续演进  
✅ **AI 辅助开发**：标准化文档让 AI 能够安全接手维护  
✅ **代码重构**：为遗留代码补充索引和规范

---

## 文档

- [核心规范](HARNESS_SPEC.md) - 完整的 Harness 工程规范
- [AI 检查清单](AI_CHECKLIST.md) - AI 维护模块的标准流程
- [AI 修复指引](AI_REPAIR_GUIDE.md) - 验证失败时的修复路径
- [主索引](INDEX.md) - 仓库结构说明
- [FAQ](FAQ.md) - 常见问题解答

---

## 版本状态

当前版本：**v1.0 Minimal** - 测试阶段

更多功能和版本正在筹备中。

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

---

**让模块化开发更规范、更可维护。**
