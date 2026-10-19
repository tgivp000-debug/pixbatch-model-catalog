# PixBatch 模型目录

这是 PixBatch 的公开模型配置仓库，仅包含模型名称、能力声明、尺寸预设和公开官方文档地址。
不包含软件源码、用户 API Key、客户授权、日志、生成图片或私钥。

## 在线地址

- 首页：https://tgivp000-debug.github.io/pixbatch-model-catalog/
- 模型配置：https://tgivp000-debug.github.io/pixbatch-model-catalog/models.json

## 当前目录

APIYi：gpt-image-2.5-all、gpt-image-2-vip、gpt-image-2.5-vip。
默认模型：gpt-image-2.5-vip。有效的已保存用户选择应优先保留。
ALL 的尺寸是提示词控制的参考值，不能视为固定像素承诺；VIP 使用独立尺寸规则。
本目录先保持 PixBatch 当前已接入的能力范围，不自动开放上游新增能力。

## 更新方式

1. 编辑 models.json；新增模型须先核对其官方文档。
2. 将 catalog_version 加 1，更新 updated_at，并补充 CHANGELOG.md。
3. 运行 python3 validate_catalog.py，确认校验通过。
4. 提交到 main，GitHub Pages 将发布更新。

## 客户端接入约定

此仓库只提供数据托管，已有 PixBatch 客户端尚未自动读取它。
客户端接入时必须校验 schema_version、字段、允许的 Provider/域名及本地已实现的 adapter。
未知 adapter 应提示升级软件，不得下载执行代码或猜测调用协议。
目录更新不得覆盖正在运行任务的配置，不得擅自切换用户已保存的有效模型。
下载/校验失败时应继续使用本地有效缓存。

在线更新使用 `models.signed.json`，由 Ed25519 签名。客户端内置公钥，校验签名后再验证目录字段。
发布时先更新 models.json，再使用私有 PixBatch 项目的 scripts/sign_model_catalog.py 签名生成
models.signed.json；二者必须一起提交。私钥位于发布者电脑 ~/.pixbatch-publisher/，绝不能提交。
客户端下载/校验后缓存，重启启用新目录，运行中任务继续使用启动时的目录快照。
