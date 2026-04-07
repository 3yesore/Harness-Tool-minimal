# AI 维护检查清单 v1.0.1 beta

AI 接手模块时，按下面顺序执行。

## 阶段 1：定位

- 读取项目 `INDEX.md`
- 找到目标模块路径
- 确认模块名称

## 阶段 2：理解合同

- 读取模块 `INDEX.md`
- 理解模块职责、关键文件、依赖
- 读取模块 `SPEC.md`
- 理解输入、输出、配置和错误边界
- 先不要读取全量源码

## 阶段 3：最小范围读取

- 只读取与当前任务直接相关的文件
- 优先看 `INDEX.md` 标出来的关键文件
- 如果需要扩展阅读，再回到模块 `INDEX.md` 确认

## 阶段 4：执行变更

- 遵循 `SPEC.md` 的接口约束
- 修改接口时先更新 `SPEC.md`
- 修改关键文件时先更新 `INDEX.md`
- 让代码与文档保持一致

## 阶段 5：验证

- 运行冒烟测试：`python tests/smoke.py`
- 确认验证通过
- 失败时先修复，再继续

## 阶段 6：记录

- 更新 `CHANGELOG.md`
- 记录变更时间
- 记录变更类型
- 必要时说明影响范围
- 如有需要，补充 `INDEX.md` 的维护信息

## 明确禁止

- 一开始就读全仓库源码
- 修改接口但不更新 `SPEC.md`
- 修改关键文件但不更新 `INDEX.md`
- 不跑测试直接收尾
- 不记录关键历史
- 用 override 绕开 contract

## 快速参考

### 校验模块

```bash
python tools/validate_module.py <module_path>
```

### 运行测试

```bash
python <module_path>/tests/smoke.py
```

### 查看规范

```bash
cat <module_path>/SPEC.md
```

## `v1.0.1 beta` 维护原则

- 先看合同，再看实现
- 先保协议，再改细节
- 先跑验证，再谈扩展
- 不把 kernel 做厚
- 不把 profile 做重
- 不把模板写成教程
- OpenHarness 相关能力保持在 bridge 层，不进入 `core`
