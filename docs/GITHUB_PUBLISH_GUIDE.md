# Harness Tool - 发布到 GitHub 完整指南

## 准备工作

### 1. 确认仓库状态

```bash
cd C:\Users\Y2516\Desktop\harness_tool

# 检查 git 状态
git status

# 查看提交历史
git log --oneline -10

# 确认所有测试通过
python examples/hello_world/tests/smoke.py
python examples/user_service/tests/smoke.py
python tools/validate_module.py examples/hello_world
python tools/validate_module.py examples/user_service
```

---

## 步骤 1: 创建 GitHub 仓库

1. 访问 https://github.com/new
2. 填写信息：
   - **Repository name**: `harness-tool-minimal`
   - **Description**: `Make modules AI-maintainable through standardized interfaces and clear indexing`
   - **Visibility**: Public
   - **不要**勾选 "Initialize this repository with"（我们已经有了）
3. 点击 "Create repository"

---

## 步骤 2: 推送到 GitHub

```bash
cd C:\Users\Y2516\Desktop\harness_tool

# 添加远程仓库（替换 YOUR_USERNAME）
git remote add origin https://github.com/YOUR_USERNAME/harness-tool-minimal.git

# 推送
git branch -M main
git push -u origin main
```

---

## 步骤 3: 完善仓库设置

### 添加 Topics
在仓库页面点击 "Add topics"，添加：
- `ai-tools`
- `code-maintenance`
- `developer-tools`
- `openclaw`
- `ai-engineering`
- `vibecoding`
- `harness-engineering`

### 设置 About
- **Description**: `Make modules AI-maintainable through standardized interfaces and clear indexing`
- **Website**: （如果有）
- **Topics**: 如上

### 启用 GitHub Actions
- 进入 "Actions" 标签
- 启用 workflows
- 确认 `.github/workflows/validate.yml` 运行成功

---

## 步骤 4: 创建 Release

1. 点击 "Releases" → "Create a new release"
2. 填写信息：
   - **Tag**: `v1.0.1-beta`
   - **Release title**: `Harness Tool Minimal v1.0.1 beta`
   - **Description**: 复制 `release/v1.0.1-beta/GITHUB_RELEASE.zh.md` 的内容
3. 点击 "Publish release"

---

## 步骤 5: 更新 README 中的链接

在 README.md 中替换所有 `YOUR_USERNAME` 为你的 GitHub 用户名：

```bash
# 使用编辑器全局替换
# YOUR_USERNAME → 你的实际用户名
```

然后提交：
```bash
git add README.md
git commit -m "Update GitHub username in README"
git push
```

---

## 步骤 6: 添加 GitHub Actions Badge

确认 Actions 运行成功后，README.md 中的 badge 会自动显示状态。

---

## 步骤 7: 创建 GitHub Discussions（可选）

1. 进入 "Settings" → "Features"
2. 启用 "Discussions"
3. 创建分类：
   - General
   - Q&A
   - Show and tell
   - Ideas

---

## 步骤 8: 添加 CODEOWNERS（可选）

创建 `.github/CODEOWNERS`：
```
* @YOUR_USERNAME
```

---

## 步骤 9: 设置 Branch Protection（可选）

1. 进入 "Settings" → "Branches"
2. 添加规则：
   - Branch name pattern: `main`
   - 勾选 "Require status checks to pass before merging"
   - 选择 "Validate Examples"

---

## 步骤 10: 分享

### 在 OpenClaw Discord 分享
```markdown
🎉 Harness Tool v1.0 发布了！

让 AI 能够跨会话、跨模型安全维护你的代码模块。

核心特性：
- 标准化的 INDEX.md + SPEC.md
- 零外部依赖，< 120KB
- 完整的 AI 操作指引
- OpenClaw Skill 集成

GitHub: https://github.com/YOUR_USERNAME/harness-tool-minimal
```

### 在相关社区发布
- Reddit: r/MachineLearning, r/programming
- Hacker News
- Twitter/X
- Dev.to

---

## 维护清单

### 定期检查
- [ ] GitHub Actions 是否正常运行
- [ ] Issues 是否及时回复
- [ ] PRs 是否及时审查

### 版本更新
- [ ] 更新 VERSION_ROADMAP.md
- [ ] 创建新的 Release
- [ ] 更新 CHANGELOG.md

---

## 故障排查

### Actions 失败
```bash
# 本地运行相同的命令
python tools/validate_module.py examples/hello_world
python examples/hello_world/tests/smoke.py
```

### Badge 不显示
- 确认 Actions 至少运行过一次
- 检查 workflow 文件名是否正确

### 推送失败
```bash
# 检查远程仓库
git remote -v

# 重新设置
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/harness-tool-minimal.git
```

---

## 下一步

1. 监控 GitHub Issues 和 Discussions
2. 收集用户反馈
3. 规划 Fetcher 版本（v2.0）
4. 完善文档和示例

---

**祝发布顺利！**
