# Profiles

Profiles 用于为不同项目类型提供不同的默认规则。

## 当前内置
- `default.rules.json`
- `python-service.rules.json`

## 未来可扩展
- `node-service.rules.json`
- `runtime-module.rules.json`
- `data-pipeline.rules.json`

## 用法
```bash
python tools/validate_module.py modules/demo --profile python-service
python tools/apply_harness.py modules/demo --profile python-service
```

Minimal 版当前只预留入口，默认仍以内置规则为主。
