# 同频 · Kiro Demo 独立复现

这是用于 Kiro Web 的私有开发交接仓库。已有 ZS-201 v0.7 Demo 由 Codex 整理为参照；Kiro 新开发尚未开始。范围只包括辅助键盘、陪伴 App、桌面小方块和合成演示接口，不包含双 Agent 配置后台。

## 让 Kiro 开始

在 Kiro Web 选中本仓库，选择 Build with spec，把 [KIRO_START.txt](KIRO_START.txt) 的内容发送给 Kiro。账号需先具备 Web 使用权限。用户不需要写代码。

为保留全部目录、隐藏的 .kiro 文件与媒体，完整交接包以 ZIP 保存。Kiro 首先运行：

```text
python3 prepare_kiro.py
```

脚本先检查 ZIP 的 SHA-256 与全部路径，再展开 90 个文件。不会调用网络、安装依赖、删除文件或覆盖内容不同的文件。重复执行可安全复用相同文件。

展开后，仓库根目录会包含 `.kiro/`、`reference-demo/`、`kiro-app/`、`docs/` 和 `package.json`。原包说明保存在 `docs/KIT_README.md`。

## 已有与待做

- 已有：61 个公开 Demo 文件、合成服务、23 项既有测试、需求/设计/任务草案、活动说明与素材来源。
- 本地已有验证：独立构建、23 项测试、资源与合成接口检查通过，详见展开后的 verification/。尚未在 Kiro 或本仓库的云环境重跑。
- 待做：Kiro 独立实现、用户选择比赛增量、新版验证与体验、提交材料。

复用的代码和素材应保留归属。合成回复/截图适配、模拟发送和实物视频不能写成真实模型、OCR、微信发送或硬件联动。是否符合活动的新作品或突破性开发要求尚待实际成果与主办方认定。

## 活动

[Kiro 鬼点子计划](https://www.infoq.cn/zones/kiro/) · [报名入口](https://www.infoq.cn/form/?id=3286)

本仓库是开发交接，不是已完成的 Kiro 参赛作品。未自动发布网站、提交报名或调用收费服务。
