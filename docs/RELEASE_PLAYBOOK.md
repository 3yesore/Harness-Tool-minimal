# 发布流程手册

这份文档是仓库后续每次发布新版本时的主流程说明。  
目标不是每次重新设计流程，而是把“版本口径对齐、文件同步、验证、打包、发布”固定成一套可以重复执行的步骤。

## 一、每次发布前先统一的口径

发布前先确认下面这些口径已经对齐：

- 仓库首页默认展示当前版本
- 当前版本使用 `v1.0.x beta` 的展示口径时，主页、文档中心、路线图、发布页、版本说明都要同步
- `v1.0.0` 只作为历史锚点保留，不再作为当前主页口径
- 默认一致性模式仍然保持 `soft`
- 扩展仍然保持“示例优先、项目本地实现”
- 版本号展示和 Git tag 命名保持区分：
  - 展示口径：`v1.0.1 beta`
  - Git tag：`v1.0.1-beta`

## 二、必须同步的文件组

每次发布新版本时，优先同步这些文件：

### 1. 仓库首页

- `README.md`
- `README.en.md`

### 2. 文档中心

- `docs/README.md`
- `docs/README.en.md`
- `docs/INDEX.md`
- `docs/INDEX.en.md`
- `docs/VERSION_ROADMAP.md`
- `docs/VERSION_ROADMAP.en.md`
- `docs/GITHUB_RELEASE.md`
- `docs/GITHUB_RELEASE.en.md`
- `docs/GITHUB_PUBLISH_GUIDE.md`

### 3. 发布资源包

- `release/v1.0.x-beta/README.md`
- `release/v1.0.x-beta/README.en.md`
- `release/v1.0.x-beta/VERSION_DESCRIPTION.zh.md`
- `release/v1.0.x-beta/VERSION_DESCRIPTION.en.md`
- `release/v1.0.x-beta/GITHUB_RELEASE.zh.md`
- `release/v1.0.x-beta/GITHUB_RELEASE.en.md`
- `release/v1.0.x-beta/DISPLAY_PAGE.zh.md`
- `release/v1.0.x-beta/DISPLAY_PAGE.en.md`
- `release/v1.0.x-beta/PUBLISH_CHECKLIST.zh.md`
- `release/v1.0.x-beta/PUBLISH_CHECKLIST.en.md`
- `release/v1.0.x-beta/UPGRADE_CHECKLIST.zh.md`
- `release/v1.0.x-beta/UPGRADE_CHECKLIST.en.md`
- `release/v1.0.x-beta/MANIFEST.md`

### 4. 版本路线图

- `docs/VERSION_ROADMAP.md`
- `docs/VERSION_ROADMAP.en.md`

## 三、发布前的最小检查顺序

每次发布建议按下面顺序走，不要跳步：

1. 先定版本号和展示口径
2. 再同步首页和文档中心
3. 再同步版本说明、展示页、升级清单和发布正文
4. 再跑验证命令
5. 再打 tag
6. 再创建 GitHub Release
7. 最后上传 release 资产包

## 四、固定验证命令

发布前建议先跑这些命令：

```bash
python tools/validate_module.py examples/hello_world --strict --profile python-service
python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service
python -m py_compile tools/init_module.py tools/apply_harness.py tools/validate_module.py
python examples/local_extension/harness/run_harness.py
```

## 五、发布页正文模板原则

发布正文不要临时乱写，尽量保持这几个部分：

- 第一段先写本次更新摘要
- 再说明这是哪个版本
- 再给版本说明链接
- 再给验证命令
- 再写风险边界
- 再明确回滚锚点

如果你希望发布页展示的是“历史基线”，就把正文口径收敛成历史展示页；  
如果你希望展示的是“新的 beta 发布”，就保留 beta 冻结口径。

## 六、升级和回滚口径

- `v1.0.0` 始终保留为历史锚点
- 当前默认展示版本写作 `v1.0.1 beta`
- Git tag 使用连字符形式：`v1.0.1-beta`
- 如果下一次是新版本，就把这三处一起改：
  - 首页
  - 文档中心
  - 发布资源包

## 七、什么时候可以发布

只有在下面几项都满足时才建议发布：

- 首页和文档中心已经对齐
- 版本说明已经写清楚
- release 资源包已经打好
- 验证命令已经通过
- 当前版本口径不会和历史版本混用

## 八、一句话总结

以后每次发布，都先改口径，再改资源，再跑验证，最后再发 release。  
这样就不用每次从头想一遍流程。
