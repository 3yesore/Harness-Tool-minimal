# Harness Tool

**让 AI 能够安全、高效地接手任何模块的维护工作。**

## 核心理念

不是让 AI 完全不依赖上下文，而是通过标准化降低依赖程度：
- 标准化输入输出接口
- 维护清晰的索引与规范
- AI 按需读取关键代码
- 支持跨会话、跨 AI 的稳定迭代

## 设计目标

1. **模块化**：每个小任务/模块都是独立单元
2. **可发现**：AI 通过索引快速定位目标模块
3. **可理解**：规范 + 少量代码阅读即可上手
4. **可维护**：支持 debug、迭代、纠错、接入/接出
5. **可定制**：harness 规范可在主仓库定义，模块轻松接入

## 快速开始

### 初始化新模块

```bash
python tools/init_module.py <module_name> [--path <output_dir>]
```

### 验证模块

```bash
python tools/validate_module.py <module_path>
```

### 查看示例

```bash
cd examples/hello_world
python tests/smoke.py
```

## 组成部分

### 1. 核心规范（HARNESS_SPEC.md）
定义 harness 工程规范：
- 索引优先
- 规范化接口
- 最小上下文
- 可验证
- 可交接

### 2. 模板（templates/）
- `INDEX.md.template`: 模块索引模板
- `SPEC.md.template`: 接口规范模板
- `CHANGELOG.md.template`: 变更历史模板

### 3. 工具（tools/）
- `init_module.py`: 初始化新模块
- `validate_module.py`: 验证模块合规性（待实现）

### 4. 示例（examples/）
- `hello_world/`: 完整的示例模块

## 模块结构

```
module_name/
├── INDEX.md           # 模块索引（必需）
├── SPEC.md            # 接口规范（必需）
├── CHANGELOG.md       # 变更历史（推荐）
├── src/               # 源代码
├── tests/             # 测试
├── configs/           # 配置
└── docs/              # 详细文档（可选）
```

## OpenClaw Skill

本仓库同时提供 OpenClaw Skill 版本，可直接在 OpenClaw 中使用：

```bash
# 安装到 OpenClaw
cp -r .openclaw_skill ~/.openclaw/skills/harness
```

详见 `.openclaw_skill/SKILL.md`

## 使用场景

- 创建需要长期维护的新模块
- 重构现有代码以便 AI 接手
- 建立项目级维护标准
- 调试文档不清晰的模块

## 与 OpenClaw Skill 的关系

本仓库借鉴了 OpenClaw Skill 的设计理念，但专注于开发场景的模块化维护：

- **OpenClaw Skill**: 为 AI 助手提供专业能力（如 PDF 处理、文档编辑）
- **Harness Tool**: 让 AI 能够维护开发项目中的模块（如业务逻辑、数据处理）

## 贡献

欢迎提交 Issue 和 PR！

## License

MIT
