# Harness 规范 v1.0

## 什么是 Harness

这里的 Harness 不是完整框架，也不是包管理器。它是一套用于模块维护的工程约定，目标是把最关键的上下文固定在少数几个文件里，让人和 AI 都能更快接手。

这份仓库里的 Harness 重点是：

- 让模块有清晰的 `INDEX.md`
- 让模块有明确的 `SPEC.md`
- 让模块有可运行的冒烟测试
- 让验证尽量自动化
- 让交接成本尽量低

## 当前仓库范围

当前实现是 Python-first，但仓库口径是模块化的，不绑定某一个业务模块。

现在已经实现的能力：

- `tools/init_module.py` 生成模块骨架
- `tools/apply_harness.py` 为现有模块补 Harness 文件和冒烟测试
- `tools/validate_module.py` 校验文档、配置和 `tests/smoke.py`
- `profiles/` 通过 `--profile` 接入脚本
- `.openclaw_skill/` 提供同样能力的 skill 包

当前还没有做深度的语言无关抽象，非 Python 模块需要额外扩展。

## 核心原则

### 1. 索引优先

- 每个维护中的模块都应该有 `INDEX.md`
- `INDEX.md` 负责说明模块职责、关键文件、依赖和验证入口
- AI 先看索引，再决定要读哪些代码

### 2. 规范化接口

- `SPEC.md` 要明确输入、输出、配置和错误处理
- 接口变化时，规范文档要先更新
- 模块实现应尽量跟着规范走，而不是让实现先漂移

### 3. 最小上下文

- 把维护必需的信息集中在少数文件里
- 不要把同一件事在多份文档里重复写很多遍
- 需要改动时，只读和任务直接相关的代码

### 4. 可验证

- 每个模块都应该有 `tests/smoke.py`
- 验证不只是看文档格式，还要真正跑测试
- 成功和失败要有明确结果

### 5. 可交接

- 交接时，接手者应该只靠 `INDEX.md`、`SPEC.md` 和冒烟测试就能理解模块
- 变更历史要能追溯
- 关键文件不要散落在太多地方

## 模块结构

### 必需文件

```text
module_name/
├── INDEX.md
├── SPEC.md
└── tests/
    └── smoke.py
```

### 推荐文件

```text
module_name/
├── CHANGELOG.md
├── src/
├── configs/
└── docs/
```

说明：

- `INDEX.md` 和 `SPEC.md` 是最低要求
- `CHANGELOG.md` 推荐保留
- `src/`、`configs/`、`docs/` 不是强制，但通常有助于维护

## INDEX.md 规范

`INDEX.md` 至少应包含这些部分：

- `## 职责`
- `## 关键文件`
- `## 依赖`
- `## 快速验证`

推荐再加：

- `## 维护注意事项`
- `## 最后更新`

快速验证部分应写出真实可执行命令，优先使用：

```bash
python tests/smoke.py
```

## SPEC.md 规范

`SPEC.md` 至少应包含这些部分：

- `## 输入`
- `## 输出`
- `## 配置`
- `## 错误处理`
- `## 示例`

规范要足够具体，至少要让维护者知道：

- 什么输入是允许的
- 什么输入会被拒绝
- 成功返回长什么样
- 失败时怎么处理

## 冒烟测试规范

冒烟测试应满足：

- 能直接用 `python tests/smoke.py` 运行
- 退出码 `0` 表示通过
- 通过时有清晰的成功提示
- 失败时有清晰的失败提示
- 覆盖模块最重要的核心路径

当前仓库的验证工具会在存在 `tests/smoke.py` 时直接执行它。

## 验证规则

当前 `tools/validate_module.py` 会做这些事：

- 检查 `INDEX.md` 和 `SPEC.md` 是否存在
- 检查 `CHANGELOG.md` 是否存在，并给出提示
- 检查 `INDEX.md` 是否包含必需章节
- 检查 `SPEC.md` 是否包含必需章节
- 检查 `configs/` 里的 JSON 是否可解析
- 检查 `tests/` 目录是否存在以及是否有 `.py` 文件
- 执行 `tests/smoke.py`
- 根据 `--profile` 检查额外的推荐文件和目录

当前 `tools/apply_harness.py` 会做这些事：

- 读取模块目录结构
- 缺少时生成 `INDEX.md`、`SPEC.md`、`CHANGELOG.md`
- 根据 profile 创建推荐目录
- 当 `tests/` 不存在或其中没有 `.py` 测试时，补一个 `tests/smoke.py`

## Profile 支持

仓库已经通过 `--profile` 接入规则文件。

当前规则文件：

- `profiles/default.rules.json`
- `profiles/python-service.rules.json`

profile 目前主要用于：

- 指定必需文件
- 指定推荐文件
- 指定推荐目录
- 指定推荐的 `INDEX.md` / `SPEC.md` 章节

profile 现在还比较轻量，更多像显式化的默认规则，不是复杂策略系统。

## 当前限制

- 目前是 Python-first
- `apply_harness.py` 仍然偏启发式，不是深度源码分析器
- 验证主要是结构检查 + 冒烟测试，不是完整语义验证
- 非 Python 模块还需要额外设计

## AI 工作流

维护 Harness 模块时，建议按这个顺序做：

1. 先读模块的 `INDEX.md`
2. 再读模块的 `SPEC.md`
3. 只按任务需要读相关代码
4. 修改实现时同步更新规范文档
5. 跑 `tests/smoke.py`
6. 跑 `tools/validate_module.py`
7. 行为变化时更新 `CHANGELOG.md`

## 版本与演进

- 当前规范版本：`v1.0`
- 现阶段目标：可用、可验证、可交接
- 后续方向：更好的源码识别、更细的 profile 差异、更多语言支持

## 参考内容

- [INDEX.md](INDEX.md)
- [README.md](README.md)
- [tools/validate_module.py](tools/validate_module.py)
- [tools/apply_harness.py](tools/apply_harness.py)
- [profiles/README.md](profiles/README.md)
- [.openclaw_skill/SKILL.md](.openclaw_skill/SKILL.md)
