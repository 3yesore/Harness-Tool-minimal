# 发布检查清单

在正式发布 `v1.0.1 beta` 之前，请逐项确认。

## 代码和验证

- [ ] `python tools/validate_module.py examples/hello_world --strict --profile python-service` 通过
- [ ] `python tools/validate_module.py examples/local_extension --strict --profile default` 通过
- [ ] `python tools/validate_module.py examples/openharness_app --strict --profile default` 通过
- [ ] `python .openclaw_skill/scripts/validate_harness.py examples/hello_world --strict --profile python-service` 通过
- [ ] `npm run build` in `C:/Users/Y2516/Desktop/openharness_app_external_verify` 通过
- [ ] `npm run smoke` in `C:/Users/Y2516/Desktop/openharness_app_external_verify` 通过

## 发布材料

- [ ] `RELEASE_NOTES_v1.0.1_beta.md` 已更新
- [ ] `release/v1.0.1-beta/VERSION_DESCRIPTION.zh.md` 已更新
- [ ] `release/v1.0.1-beta/VERSION_DESCRIPTION.en.md` 已更新
- [ ] `release/v1.0.1-beta/GITHUB_RELEASE.zh.md` 已更新
- [ ] `release/v1.0.1-beta/GITHUB_RELEASE.en.md` 已更新
- [ ] 发布口径与当前版本状态一致

## 仓库状态

- [ ] 已按 freeze groups 完成分组提交
- [ ] 没有遗漏的临时文件或缓存目录
- [ ] `examples/openharness_app/node_modules/` 未进入版本控制
- [ ] `harness_core/` 保持薄核心，没有新增 runtime 托管逻辑
- [ ] OpenHarness 兼容能力仍停留在 bridge / binding 外层
- [ ] 默认一致性模式仍然保留 `soft`

## 发布后动作

- [ ] 打上版本标签 `v1.0.1-beta`
- [ ] 保留 `v1.0.0` 作为回滚锚点
- [ ] 检查 README / SPEC / skill mirror / bridge 文档是否与已发布行为一致
