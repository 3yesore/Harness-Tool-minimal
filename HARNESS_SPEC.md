# Harness 规范 v1.0

## 什么是 Harness?

Harness 是一套让 AI 能够安全、高效接手模块维护的工程规范。

**核心目标**: 通过标准化降低 AI 对上下文的依赖,支持跨会话、跨模型的稳定迭代。

## 设计原则

### 1. 索引优先 (Index-First)
- 每个模块必须有清晰的 INDEX.md
- 索引说明模块职责、关键文件、依赖关系
- AI 通过索引快速定位,而非全量扫描代码

**为什么**: 减少 AI 需要阅读的代码量,提高定位效率。

### 2. 规范化接口 (Standardized Interface)
- 输入输出必须标准化并文档化
- 配置与代码分离
- 错误处理统一

**为什么**: 让 AI 能够安全修改代码,降低引入 bug 的风险。

### 3. 最小上下文 (Minimal Context)
- 关键信息集中在索引与规范
- 代码按需阅读
- 避免冗余文档

**为什么**: 节省 token,提高 AI 响应速度。

### 4. 可验证 (Verifiable)
- 每个模块必须有验证方式
- 支持快速冒烟测试
- 明确的成功/失败标准

**为什么**: 让 AI 能够自主验证改动,无需人工介入。

### 5. 可交接 (Handoff-Ready)
- 新 AI 能通过索引 + 规范快速上手
- 支持跨会话、跨 AI 的迭代
- 变更历史可追溯

**为什么**: 保证长期维护的连续性。

## 模块结构

### 必需文件

```
module_name/
├── INDEX.md           # 模块索引(必需)
├── SPEC.md            # 接口规范(必需)
└── tests/             # 测试目录(必需)
    └── smoke.py       # 至少一个冒烟测试
```

### 推荐文件

```
module_name/
├── CHANGELOG.md       # 变更历史(推荐)
├── src/               # 源代码
├── configs/           # 配置文件
└── docs/              # 详细文档(可选)
```

## INDEX.md 规范

### 必需章节

```markdown
# Module: [模块名]

## 职责
[一句话说明模块做什么]

## 关键文件
- `src/main.py`: 入口
- `configs/default.json`: 默认配置
- `tests/smoke.py`: 冒烟测试

## 依赖
- 外部依赖: [列出 pip/npm 包]
- 内部依赖: [列出其他模块]

## 快速验证
\`\`\`bash
python tests/smoke.py
\`\`\`
```

### 推荐章节

```markdown
## 维护注意事项
[列出关键约束、已知问题、特殊配置等]

## 最后更新
- 日期: YYYY-MM-DD
- 变更: [简要描述]
```

## SPEC.md 规范

### 必需章节

```markdown
# 接口规范: [模块名]

## 输入
### 参数
\`\`\`json
{
  "param1": "string",
  "param2": 123
}
\`\`\`

### 约束
- `param1`: 必需,非空字符串
- `param2`: 可选,默认 0

## 输出
### 成功响应
\`\`\`json
{
  "status": "success",
  "data": {}
}
\`\`\`

### 错误响应
\`\`\`json
{
  "status": "error",
  "code": "ERROR_CODE",
  "message": "错误描述"
}
\`\`\`

## 配置
### 配置文件: `configs/default.json`
\`\`\`json
{
  "timeout": 30
}
\`\`\`

## 错误处理
- 输入验证失败: 返回 `INVALID_INPUT`
- 运行时异常: 返回 `RUNTIME_ERROR`

## 示例
### Python
\`\`\`python
from module_name import run
result = run(param1="value")
\`\`\`
```

## 测试规范

### 冒烟测试要求

1. **必须可执行**: `python tests/smoke.py` 能直接运行
2. **明确输出**: 清晰的成功/失败提示
3. **快速完成**: 通常 < 10 秒
4. **覆盖核心**: 测试关键功能路径

### 示例

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""模块冒烟测试"""

def test_basic():
    result = module.run()
    assert result["status"] == "success"
    print("[PASS] 基础功能测试通过")

if __name__ == "__main__":
    test_basic()
    print("\n[SUCCESS] 所有测试通过")
```

## AI 工作流

当 AI 维护 harness 模块时,应遵循以下流程:

### 1. 定位模块
- 读取项目主 INDEX.md
- 找到目标模块路径

### 2. 理解接口
- 读取模块的 INDEX.md (职责、关键文件、依赖)
- 读取模块的 SPEC.md (输入输出、配置、错误处理)
- **不要**一开始就读全部代码

### 3. 按需读码
- 根据任务只读取相关代码文件
- 参考 INDEX.md 的"关键文件"章节

### 4. 执行变更
- 遵循 SPEC.md 的接口约束
- 保持输入输出格式不变(除非明确要求修改接口)
- 更新相关文档

### 5. 验证结果
- 运行冒烟测试: `python tests/smoke.py`
- 确保测试通过

### 6. 记录变更
- 更新 CHANGELOG.md
- 更新 INDEX.md 的"最后更新"

## 验证工具

使用 `validate_module.py` 检查模块合规性:

```bash
python tools/validate_module.py <module_path>
```

验证项:
- ✅ 必需文件存在 (INDEX.md, SPEC.md, tests/)
- ✅ INDEX.md 包含必需章节
- ✅ SPEC.md 包含必需章节
- ✅ 测试目录非空
- ✅ 配置文件格式正确

## 规范演进

### 版本控制
- 当前版本: v1.0
- 版本号格式: `v主版本.次版本`
- 主版本变更: 不兼容的规范修改
- 次版本变更: 向后兼容的增强

### 变更流程
1. 提交 Issue 讨论变更提案
2. 通过 PR 提交规范修改
3. 更新所有受影响的模块
4. 发布新版本

### 兼容性承诺
- 新版本必须向后兼容旧模块
- 废弃功能至少保留一个主版本
- 提供迁移指南

## 常见问题

### Q: 必须使用 Python 吗?
A: 不,Harness 规范与语言无关。示例使用 Python 只是为了演示。

### Q: 可以修改模板吗?
A: 可以,但必须保留必需章节。

### Q: 如何处理大型模块?
A: 考虑拆分成多个子模块,每个遵循 Harness 规范。

### Q: 需要为每个函数写 SPEC 吗?
A: 不,SPEC.md 只定义模块的公开接口。

## 参考资源

- [示例模块](../examples/hello_world/) - 完整参考实现
- [模板文件](../templates/) - INDEX/SPEC/CHANGELOG 模板
- [OpenClaw Skill](../.openclaw_skill/SKILL.md) - OpenClaw 集成
