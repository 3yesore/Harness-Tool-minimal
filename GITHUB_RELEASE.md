# Harness Tool - 发布到 GitHub 指南

## 1. 创建 GitHub 仓库

1. 访问 https://github.com/new
2. 仓库名称：`harness-tool`
3. 描述：`Make modules AI-maintainable through standardized interfaces and clear indexing`
4. 选择 Public
5. 不要初始化 README（我们已经有了）
6. 点击 "Create repository"

## 2. 推送到 GitHub

```bash
cd C:\Users\Y2516\Desktop\harness_tool

# 添加远程仓库（替换 YOUR_USERNAME）
git remote add origin https://github.com/YOUR_USERNAME/harness-tool.git

# 推送
git branch -M main
git push -u origin main
```

## 3. 完善 GitHub 仓库

### 添加 Topics
在仓库页面点击 "Add topics"，添加：
- `ai-tools`
- `code-maintenance`
- `developer-tools`
- `openclaw`
- `ai-engineering`

### 添加 About
- Description: `Make modules AI-maintainable through standardized interfaces and clear indexing`
- Website: （如果有）
- Topics: 如上

### 创建 Release
1. 点击 "Releases" -> "Create a new release"
2. Tag: `v1.0.0`
3. Title: `Harness Tool v1.0.0`
4. Description:
```markdown
## 🎉 Initial Release

Harness Tool v1.0 提供了一套完整的工程规范，让 AI 能够安全、高效地接手模块维护。

### ✨ 核心特性

- 📋 标准化模块结构（INDEX.md + SPEC.md）
- 🔧 模块初始化工具
- ✅ 合规性验证工具
- 📦 OpenClaw Skill 集成
- 📚 完整示例（hello_world）

### 🚀 快速开始

\`\`\`bash
# 初始化新模块
python tools/init_module.py my_module

# 验证模块
python tools/validate_module.py modules/my_module
\`\`\`

### 📖 文档

- [核心规范](HARNESS_SPEC.md)
- [示例模块](examples/hello_world/)
- [OpenClaw Skill](.openclaw_skill/SKILL.md)
```

## 4. 可选：添加 GitHub Actions

创建 `.github/workflows/validate.yml` 用于自动验证：

```yaml
name: Validate Examples

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Run hello_world tests
        run: python examples/hello_world/tests/smoke.py
```

## 5. 分享

- 在 OpenClaw Discord 分享
- 在相关社区发布
- 添加到 awesome-ai-tools 列表
