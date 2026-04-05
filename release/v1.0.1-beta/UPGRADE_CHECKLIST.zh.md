# 从旧版本升级到 v1.0.1 beta 的覆盖清单

这份清单的目标很简单：  
如果你想把现有仓库升级到 `v1.0.1 beta` 的 minimal 基线，就尽量只覆盖公共底座、标准文档和发布资源，不要把你自己的业务代码和项目定制一起覆盖掉。

## 一、建议覆盖的文件

如果你的目标是“让仓库整体切到 v1.0.1 beta 的口径”，建议覆盖下面这些文件和目录：

### 1. 根目录发布口径

- `README.md`
- `README.en.md`
- `VERSION_ROADMAP.md`
- `VERSION_ROADMAP.en.md`
- `GITHUB_RELEASE.md`
- `GITHUB_RELEASE.en.md`

### 2. 仓库文档中心

- `docs/README.md`
- `docs/README.en.md`
- `docs/INDEX.md`
- `docs/INDEX.en.md`
- `docs/HARNESS_SPEC.md`
- `docs/HARNESS_SPEC.en.md`
- `docs/GITHUB_RELEASE.md`
- `docs/GITHUB_RELEASE.en.md`
- `docs/GITHUB_PUBLISH_GUIDE.md`
- `docs/VERSION_ROADMAP.md`
- `docs/VERSION_ROADMAP.en.md`
- `docs/EXTENSION_POINTS.md`
- `docs/EXTENSION_POINTS.en.md`
- `docs/AI_CHECKLIST.md`
- `docs/AI_OPERATIONS.md`
- `docs/AI_OPERATIONS.en.md`

### 3. 工具与标准化入口

- `tools/init_module.py`
- `tools/apply_harness.py`
- `tools/validate_module.py`
- `.openclaw_skill/SKILL.md`
- `.openclaw_skill/scripts/`
- `.openclaw_skill/templates/`
- `.openclaw_skill/references/`
- `.openclaw_skill/profiles/`

### 4. 扩展面和默认模板

- `profiles/`
- `templates/`
- `examples/hello_world/`
- `examples/local_extension/`，如果你希望把本地扩展示例一起带到 beta 口径

### 5. 发布资源

- `release/v1.0.1-beta/`

## 二、不要动的文件

下面这些内容通常不应该直接覆盖，否则很容易把你自己的项目内容一起清掉：

- 你自己的业务模块目录
- 你自己写的项目级配置文件
- 你自己定制过的测试文件
- 你自己的 `.env`、密钥、凭据文件
- 你自己维护的 CI / 发布流程文件，除非你明确要统一到这版仓库口径
- 任何已经包含业务逻辑的源代码目录

如果你的仓库里有类似下面这种目录，也应该先确认它们是不是项目定制，而不是官方示例：

- `modules/`
- `src/`
- `app/`
- `service/`
- `worker/`
- `domain/`

这些目录如果已经有业务代码，优先保留。

## 三、升级策略

### 方案 A：只想对齐 beta 口径

适合你只想让文档、模板、工具、skill 包和发布说明对齐 `v1.0.1 beta`。

建议覆盖：

- 根目录 README
- `docs/`
- `tools/`
- `.openclaw_skill/`
- `profiles/`
- `templates/`
- `release/v1.0.1-beta/`

### 方案 B：想把 minimal 基线整体带过去

适合你想让新安装或新分支直接具备这版 minimal 效果。

建议覆盖：

- 方案 A 的全部内容
- `examples/hello_world/`
- `examples/local_extension/`
- 如果仓库里有核心共享底座目录，也一并同步到 beta 口径

### 方案 C：保留项目定制，只同步公共底座

适合你已经在原仓库上做了较多定制，只想把公共基础设施升级。

建议覆盖：

- `README.md` / `README.en.md`
- `docs/`
- `tools/`
- `.openclaw_skill/`
- `profiles/`
- `templates/`
- `release/v1.0.1-beta/`

不要覆盖：

- 你自己的业务目录
- 你自己加的模块
- 你自己的测试和配置

## 四、升级顺序建议

推荐按这个顺序覆盖，能减少口径漂移：

1. 先覆盖文档和发布说明
2. 再覆盖 `tools/` 和 `.openclaw_skill/`
3. 再覆盖 `profiles/` 和 `templates/`
4. 需要的话再覆盖示例目录
5. 最后检查 `release/v1.0.1-beta/` 的 release 资源是否完整

## 五、升级后要检查什么

- `README` 的版本号是否已经切到 `v1.0.1 beta`
- `VERSION_ROADMAP` 是否仍然指向旧版本
- `docs/INDEX.md` 和 `docs/HARNESS_SPEC.md` 是否还残留旧口径
- `tools/validate_module.py`、`tools/apply_harness.py`、`tools/init_module.py` 是否和 skill 包一致
- `profiles/` 和 `templates/` 是否仍然是轻量预设，而不是被改成厚策略系统
- `release/v1.0.1-beta/` 是否仍然包含中英文版本说明和发布资源

## 六、最关键的一句话

如果你要的是 `v1.0.1 beta` 的 minimal 效果，优先覆盖公共底座和发布资源；  
如果你要保留自己的项目定制，就不要动业务目录和已有定制文件。
