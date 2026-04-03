# Harness Tool 主索引

## 仓库结构

```
harness_tool/
├── README.md              # 项目说明
├── HARNESS_SPEC.md        # 核心规范
├── INDEX.md               # 本文件：主索引
├── templates/             # 模块模板
├── tools/                 # 工具脚本
├── examples/              # 示例模块
└── modules/               # 实际模块（未来）
```

## 核心文件

- `HARNESS_SPEC.md`: 定义 harness 规范，AI 必读
- `templates/`: 新建模块时使用的模板
- `tools/init_module.py`: 初始化新模块的脚本

## 快速开始

### 创建新模块
```bash
python tools/init_module.py <module_name>
```

### 接入现有模块
1. 在模块根目录添加 INDEX.md 和 SPEC.md
2. 遵循 HARNESS_SPEC.md 规范
3. 更新本文件的模块清单

## 模块清单

（暂无，待添加）

## 维护指南

- 所有模块必须遵循 HARNESS_SPEC.md
- 新增模块后更新本索引
- 规范变更需要更新所有模块
