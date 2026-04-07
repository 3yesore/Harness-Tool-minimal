# Module: hello_world

## 职责
展示 Harness Tool 最小协议的标准示例模块。

## 关键文件
- `src/main.py`: 入口，打印 hello world
- `tests/smoke.py`: 冒烟测试
- `configs/default.json`: 默认配置

## 调用入口
- `module_name`: `hello_world`
- `entry_file`: `src/main.py`
- `call_path`: `src/main.py`
- `call_entry`: `src/main.py`

## 关键标记
- `entry_file`: `src/main.py`
- `call_path`: `src/main.py`
- `call_entry`: `src/main.py`

## 依赖
- 外部依赖: 无
- 内部依赖: 无

## 快速验证
```bash
python tests/smoke.py
```

## 维护注意事项
- 这是一个示例模块，用于验证 harness 协议。
- 真实模块应继续补充业务逻辑和测试。

## 变更记录
- 日期: 2026-04-03
- 说明: 初始化示例模块
