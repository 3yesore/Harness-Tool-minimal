# FAQ - 常见问题

## 基础问题

### Q: Harness Tool 是什么？
A: 一套让 AI 能够跨会话、跨模型安全维护模块的工程规范和工具集。

### Q: 为什么需要 Harness Tool？
A: 解决 AI 维护代码时的三大痛点：
1. 每次都要重新理解整个项目
2. 缺少标准化接口，容易引入 bug
3. 换个 AI 或新会话就要重新开始

### Q: Harness Tool 适合我吗？
A: 如果你：
- 使用 AI 辅助开发（vibecoding）
- 需要频繁切换 AI 模型或会话
- 希望代码可被 AI 长期维护
- 不想引入复杂工具链

那么 Harness Tool Minimal 很适合你。

---

## 使用问题

### Q: 如何开始使用？
A: 三步：
```bash
# 1. 初始化新模块
python tools/init_module.py my_module

# 2. 补充 INDEX.md 和 SPEC.md
# 3. 验证
python tools/validate_module.py my_module
```

### Q: 已有项目如何接入？
A: 使用 apply_harness.py：
```bash
python tools/apply_harness.py existing_module
```
然后人工补充 INDEX.md 和 SPEC.md 的实际内容。

### Q: 必须严格遵循规范吗？
A: 核心规范（INDEX.md + SPEC.md + tests/）必须遵循，其他可灵活调整。

### Q: 可以自定义规范吗？
A: 可以，通过 `profiles/` 目录自定义规则，但 Minimal 版当前只预留了接口。

---

## 技术问题

### Q: INDEX.md 和 SPEC.md 有什么区别？
A: 
- **INDEX.md**: 模块索引，告诉 AI"这个模块是什么、关键文件在哪"
- **SPEC.md**: 接口规范，告诉 AI"输入输出是什么、如何调用"

### Q: 为什么不用自动生成工具？
A: Harness Tool 的理念是"通过规范赋能 AI"，而非"代替 AI 判断"。自动生成的文档往往不准确，反而增加维护负担。

### Q: 测试必须写吗？
A: 是的。tests/smoke.py 是验证模块正确性的最后防线，也是 AI 修改后的验证手段。

### Q: 支持哪些编程语言？
A: Harness 规范与语言无关。示例使用 Python 只是为了演示，你可以用任何语言。

---

## 对比问题

### Q: 和 OpenClaw Skill 有什么区别？
A: 
- **OpenClaw Skill**: 为 AI 助手提供专业能力（如 PDF 处理）
- **Harness Tool**: 让 AI 能够维护你的开发项目模块

### Q: Minimal / Fetcher / Intruder 有什么区别？
A: 
- **Minimal**: 核心规范 + 基础工具，零依赖
- **Fetcher**: 为 Codex/Claude 优化，高度自定义
- **Intruder**: 企业级，CI/CD + 审计 + 团队协作

### Q: 和传统文档有什么区别？
A: 传统文档是给人看的，Harness 文档是给 AI 看的：
- 结构化、标准化
- 强制索引和接口定义
- 可验证、可测试

---

## 进阶问题

### Q: 如何处理大型模块？
A: 考虑拆分成多个子模块，每个遵循 Harness 规范。

### Q: 如何管理模块间依赖？
A: 在 INDEX.md 的"依赖"章节声明，Standard 版会提供依赖图工具。

### Q: 验证失败怎么办？
A: 参考 `AI_REPAIR_GUIDE.md`，按问题类型逐个修复。

### Q: 可以用于生产环境吗？
A: 可以。Harness Tool 只是文档规范，不影响代码运行。

---

## 贡献问题

### Q: 如何贡献？
A: 参考 `CONTRIBUTING.md`。

### Q: 可以提议修改规范吗？
A: 可以，但需要：
1. 先在 Issue 讨论
2. 保持向后兼容
3. 更新所有示例

### Q: 发现 bug 怎么办？
A: 在 GitHub Issues 报告，提供复现步骤。

---

## 其他问题

### Q: 有社区吗？
A: 
- GitHub Discussions
- OpenClaw Discord

### Q: 有商业支持吗？
A: Minimal 版完全开源免费，Enterprise 版（Intruder）未来可能提供商业支持。

### Q: 路线图是什么？
A: 参考 `VERSION_ROADMAP.md`。
