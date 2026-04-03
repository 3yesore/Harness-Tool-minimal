# Harness Tool 主索引

## 仓库概览

Harness Tool Minimal 是一套轻量级工程规范,让 AI 能够通过标准化接口安全接手模块维护。

## 仓库结构

```
harness_tool/
├── README.md              # 项目说明
├── HARNESS_SPEC.md        # 核心规范(AI 必读)
├── INDEX.md               # 本文件:主索引
├── VERSION_ROADMAP.md     # 版本规划
├── GITHUB_RELEASE.md      # GitHub 发布指南
├── LICENSE                # MIT 许可证
├── .gitignore             # Git 忽略规则
│
├── templates/             # 模块模板
│   ├── INDEX.md.template
│   ├── SPEC.md.template
│   └── CHANGELOG.md.template
│
├── tools/                 # 工具脚本
│   ├── init_module.py     # 初始化新模块
│   └── validate_module.py # 验证模块合规性
│
├── examples/              # 示例模块
│   └── hello_world/       # 完整示例
│       ├── INDEX.md
│       ├── SPEC.md
│       ├── src/main.py
│       ├── tests/smoke.py
│       └── configs/default.json
│
└── .openclaw_skill/       # OpenClaw Skill 版本
    ├── SKILL.md
    ├── scripts/
    └── references/
```

## 核心文件说明

### 规范文档
- **HARNESS_SPEC.md**: 定义 harness 工程规范,AI 维护模块时必读
- **VERSION_ROADMAP.md**: Minimal/Standard/Enterprise 三版本规划

### 模板文件
- **templates/INDEX.md.template**: 模块索引模板
- **templates/SPEC.md.template**: 接口规范模板
- **templates/CHANGELOG.md.template**: 变更历史模板

### 工具脚本
- **tools/init_module.py**: 初始化新模块,自动生成标准结构
- **tools/validate_module.py**: 验证模块是否符合 Harness 规范

### 示例模块
- **examples/hello_world/**: 完整的参考实现,展示所有规范要求

## 快速开始

### 创建新模块
```bash
python tools/init_module.py <module_name> [--path <output_dir>]
```

### 验证模块
```bash
python tools/validate_module.py <module_path>
```

### 运行示例
```bash
cd examples/hello_world
python tests/smoke.py
```

## 接入现有模块

1. 在模块根目录创建 INDEX.md (参考 templates/INDEX.md.template)
2. 创建 SPEC.md 定义接口 (参考 templates/SPEC.md.template)
3. 添加 tests/ 目录和冒烟测试
4. 运行 `python tools/validate_module.py <module_path>` 验证
5. 更新本文件的模块清单

## 模块清单

### 示例模块
- `examples/hello_world/`: 演示 harness 规范的最小示例

### 实际模块
(暂无,待添加)

## 维护指南

### 添加新模块
1. 使用 `init_module.py` 初始化
2. 实现功能并添加测试
3. 运行 `validate_module.py` 确保合规
4. 更新本索引的模块清单

### 修改现有模块
1. 读取模块的 INDEX.md 和 SPEC.md
2. 按需读取相关代码文件
3. 遵循 SPEC 约束进行修改
4. 运行测试验证
5. 更新 CHANGELOG.md

### 规范变更
- 所有模块必须遵循 HARNESS_SPEC.md
- 规范变更需要更新所有模块
- 保持向后兼容

## OpenClaw Skill

本仓库同时提供 OpenClaw Skill 版本,详见 `.openclaw_skill/SKILL.md`

安装方法:
```bash
cp -r .openclaw_skill ~/.openclaw/skills/harness
```

## 版本信息

- 当前版本: v1.0.0 Minimal
- 规范版本: v1
- 最后更新: 2026-04-03
