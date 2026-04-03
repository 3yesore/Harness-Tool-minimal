# Harness Tool 扩展接口预留

这份文档定义 Minimal 版本为 Standard / Enterprise 预留的扩展点。

## 设计目标

Minimal 版不直接做复杂平台化，但接口先留好，避免后续重构工具入口。

## 扩展点一：Profile

用途：按项目类型切换校验和骨架生成策略。

### 当前预留
- `validate_module.py --profile <name>`
- `apply_harness.py --profile <name>`

### 未来可扩展
- `python-service`
- `node-service`
- `runtime-module`
- `data-pipeline`

### 约定
Profile 只负责：
- 默认模板偏好
- 必需文件差异
- 推荐目录差异
- 校验强度差异

Profile 不负责执行任意代码。

---

## 扩展点二：Rules Config

用途：让项目可自定义规则，而不是把所有规则硬编码进工具。

### 当前预留
- `validate_module.py --rules-config <path>`
- `apply_harness.py --rules-config <path>`

### 配置文件建议格式
```json
{
  "required_files": ["INDEX.md", "SPEC.md"],
  "recommended_files": ["CHANGELOG.md"],
  "required_index_sections": ["## 职责", "## 关键文件", "## 依赖", "## 快速验证"],
  "required_spec_sections": ["## 输入", "## 输出", "## 配置", "## 错误处理", "## 示例"]
}
```

### 约束
- Minimal 版只读取配置，不执行插件脚本
- 配置优先级：CLI > 项目本地 > 内置默认

---

## 扩展点三： Machine-readable Report

用途：后续给 CI、Dashboard、批量治理工具消费。

### 当前预留
- `validate_module.py --json`

### 输出结构
```json
{
  "module_path": "modules/demo",
  "profile": "default",
  "errors": [],
  "warnings": [],
  "checks": [
    {"name": "required_files", "status": "pass"}
  ]
}
```

---

## 扩展点四： Skeleton Strategy

用途：对不同项目类型生成不同 INDEX / SPEC 骨架。

### 当前预留
- `apply_harness.py --profile <name>`
- `apply_harness.py --dry-run`

### 未来方向
- 标准服务模块骨架
- Runtime 控制器骨架
- 数据处理模块骨架
- Adapter / Connector 模块骨架

---

## 扩展点五： Project-level Harness

用途：Standard 版做多模块治理时复用。

### 当前约定
Minimal 只管单模块，但保留项目级入口：
- 项目主 `INDEX.md`
- 模块级 `INDEX.md`
- 模块级 `SPEC.md`

### Standard 版可在此基础增加
- 项目总索引自动生成
- 依赖关系图
- 批量校验
- 模块健康度报告

---

## 当前边界

Minimal 版刻意不做这些事：
- 不执行任意外部插件
- 不引入复杂依赖图系统
- 不做自动代码理解/自动补全真实接口
- 不做 CI 平台耦合

这样可以保持：
- 轻
- 稳
- 可解释
- 易迁移到 GitHub
