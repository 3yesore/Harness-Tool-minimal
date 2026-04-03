# Harness Tool Minimal

面向模块维护的 Harness Engineering 工具。

它把 `INDEX.md`、`SPEC.md`、`tests/smoke.py` 和变更记录收拢成一套可验证、可交接的最小闭环。

## 亮点

- 最小闭环：初始化、接入、验证、记录
- 真实可执行：`validate_module.py` 会实际运行 `tests/smoke.py`
- 双语文档：中文主入口 + 英文镜像
- 可扩展：`profiles/`、`.openclaw_skill/`、`templates/`
- 可发布：已整理到适合同步 GitHub 的状态

## 快速上手

```bash
python tools/init_module.py my_module
python tools/apply_harness.py path/to/module --profile python-service
python tools/validate_module.py path/to/module --strict --profile python-service
```

## 内容

- `tools/init_module.py` 新建模块骨架
- `tools/apply_harness.py` 为现有模块补 Harness
- `tools/validate_module.py` 校验文档、配置和冒烟测试
- `templates/` 模板
- `profiles/` 规则预设
- `examples/` 参考示例
- `.openclaw_skill/` OpenClaw / Codex skill 包

## 示例

- `examples/hello_world`
- `examples/user_service`

## 安装 Skill

### OpenClaw

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.openclaw\skills" | Out-Null
Copy-Item -Recurse -Force ".openclaw_skill" "$env:USERPROFILE\.openclaw\skills\harness"
```

### Codex / VS Code

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".openclaw_skill" "$env:USERPROFILE\.codex\skills\harness"
```

## 文档

- [INDEX.md](INDEX.md)
- [HARNESS_SPEC.md](HARNESS_SPEC.md)
- [GITHUB_RELEASE.md](GITHUB_RELEASE.md)
- [VERSION_ROADMAP.md](VERSION_ROADMAP.md)
- [README.en.md](README.en.md)

## 当前状态

测试阶段，后续功能和适配还在更新，欢迎反馈。
