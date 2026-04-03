# AI 修复指引

当 Harness 模块验证失败时，不要优先写“自动修复器”。

先按这份指引，让 AI 自己完成诊断、修复、验证、记录。

---

## 原则

1. **先诊断，再修改**
2. **只修当前验证失败相关项**
3. **修完必须重新验证**
4. **修完必须更新 CHANGELOG.md**
5. **能通过规范修复的，不优先引入额外工具**

---

## 标准修复流程

### Step 1: 运行验证器

```bash
python tools/validate_module.py <module_path>
```

把输出里的问题分为两类：
- `ERROR`：必须修
- `WARN`：建议修

---

### Step 2: 按问题类型修复

## A. 缺少 INDEX.md

### 处理方法
```bash
python tools/apply_harness.py <module_path>
```

然后人工/AI 补全：
- `## 职责`
- `## 关键文件`
- `## 依赖`
- `## 快速验证`

### 修完后检查
- INDEX.md 是否真实反映当前模块，而不是模板残留

---

## B. 缺少 SPEC.md

### 处理方法
```bash
python tools/apply_harness.py <module_path>
```

然后人工/AI 补全：
- 输入参数
- 输出结构
- 错误处理
- 配置项
- 示例

### 修完后检查
- SPEC.md 写的是“真实接口”，不是占位内容

---

## C. 缺少 CHANGELOG.md

### 处理方法
新建 `CHANGELOG.md`，至少包含：

```markdown
# Changelog: module_name

## [1.0.0] - YYYY-MM-DD
### Added
- 初始化或补齐 harness 文档
```

### 修完后检查
- 是否有日期
- 是否有版本号

---

## D. INDEX.md 缺少章节

### 处理方法
补齐以下必需章节：
- `## 职责`
- `## 关键文件`
- `## 依赖`
- `## 快速验证`

### 修完后检查
- 标题名必须完全匹配

---

## E. SPEC.md 缺少章节

### 处理方法
补齐以下必需章节：
- `## 输入`
- `## 输出`
- `## 配置`
- `## 错误处理`
- `## 示例`

### 修完后检查
- 标题名必须完全匹配

---

## F. 关键文件路径不存在

### 处理方法
先判断是哪一种情况：

#### 情况 1：文档写错了
更新 INDEX.md 中的路径为真实路径。

#### 情况 2：文件应该存在但缺失
补回对应文件。

### 判断原则
- 如果代码入口已经换位置 → 改 INDEX.md
- 如果测试文件本来就应该有 → 补测试文件
- 如果配置本应存在 → 补配置文件

### 修完后检查
- INDEX.md 中每个反引号路径都应真实存在

---

## G. 快速验证命令引用的文件不存在

### 处理方法
修 `## 快速验证` 里的命令，让它引用当前模块真实存在的测试文件。

### 推荐写法
在模块目录内部执行时：
```bash
python tests/smoke.py
```

如果必须从项目根运行：
```bash
python <module_path>/tests/smoke.py
```

### 修完后检查
- 命令中的脚本路径真实存在
- 命令能实际跑通

---

## H. tests/ 目录不存在

### 处理方法
创建：
```bash
mkdir <module_path>/tests
```

再补一个最小冒烟测试：
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def test_basic():
    print("[PASS] 基础功能测试通过")


if __name__ == "__main__":
    test_basic()
    print("\n[SUCCESS] 所有测试通过")
```

### 修完后检查
- `python tests/smoke.py` 可运行

---

## I. configs/ 不存在

### 处理方法
先判断：
- 如果模块确实不需要配置：可不创建，接受 warning
- 如果模块需要配置：创建 `configs/` 并补默认配置

### 原则
不要为了消 warning 机械建空目录。

---

## Step 3: 重新验证

```bash
python tools/validate_module.py <module_path>
```

目标：
- 至少消除全部 `ERROR`
- 能修的 `WARN` 尽量修掉

---

## Step 4: 运行测试

```bash
cd <module_path>
python tests/smoke.py
```

如果测试失败：
- 先修测试或实现
- 不要跳过

---

## Step 5: 更新变更记录

修完后更新：
- `CHANGELOG.md`
- `INDEX.md` 的“最后更新”

推荐记录：
```markdown
### Fixed
- 补齐 INDEX.md 必需章节
- 修正快速验证命令路径
- 增加 tests/smoke.py
```

---

## AI 修复输出模板

修复完成后，建议 AI 用这个格式汇报：

```markdown
## 修复结果
- 模块：<module_path>
- 已修复：
  - 缺少 SPEC.md
  - 快速验证路径错误
  - 缺少 CHANGELOG.md
- 验证结果：通过 / 仍有警告
- 测试结果：通过 / 失败
- 剩余风险：<如果有>
```

---

## 为什么不优先做自动修复器

因为 Harness Tool 的目标不是“代替 AI 判断”，而是：
- 给 AI 清晰规则
- 给 AI 标准修复路径
- 让 AI 在低上下文下也能稳定完成维护

如果一个问题必须靠额外修复器才能解决，反而说明规范本身不够硬。

所以 Minimal 版更合理的做法是：
- 提供**验证器**
- 提供**应用骨架工具**
- 提供**修复指引**

而不是继续堆自动修复逻辑。
