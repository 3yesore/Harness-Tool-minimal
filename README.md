# Harness Tool Minimal

面向模块维护的 Harness Engineering 工具。

它把 `INDEX.md`、`SPEC.md`、`tests/smoke.py` 和变更记录收拢成一套可验证、可交接的最小闭环，适合长期维护的模块，也适合需要 AI 接手的项目。

## 亮点

- 最小闭环：初始化、接入、验证、记录，一条链路跑通
- 真实可执行：`validate_module.py` 会实际运行 `tests/smoke.py`
- 双语文档：中文主入口 + 英文镜像
- 可扩展：`profiles/`、`.openclaw_skill/`、`templates/` 都已预留
- 可发布：仓库已整理到适合同步 GitHub 的状态

## 适合谁

- 想把模块交给 AI 长期维护的人
- 想给遗留代码补最小可维护结构的人
- 想让项目改动后有固定验证入口的人
- 想把模块做成交接友好形态的人
- 想把同一套 skill 同时装到 OpenClaw 和 Codex 的人

## 3 分钟上手

```bash
python tools/init_module.py my_module
python tools/apply_harness.py path/to/module --profile python-service
python tools/validate_module.py path/to/module --strict --profile python-service
```

## 它包含什么

- `tools/init_module.py`：新建模块骨架
- `tools/apply_harness.py`：为现有模块补 Harness
- `tools/validate_module.py`：校验文档、配置和冒烟测试
- `templates/`：模板
- `profiles/`：规则预设
- `examples/`：参考示例
- `.openclaw_skill/`：可安装到 OpenClaw / Codex 的 skill 包

## 参考示例

- `examples/hello_world`：最小可验证示例
- `examples/user_service`：更接近真实项目的示例

## Skill 安装

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

## 下一步

1. 打开 [INDEX.md](INDEX.md) 看仓库结构
2. 打开 [HARNESS_SPEC.md](HARNESS_SPEC.md) 看规范
3. 先跑 `examples/hello_world/tests/smoke.py`
4. 再跑 `python tools/validate_module.py examples/hello_world --strict --profile python-service`
