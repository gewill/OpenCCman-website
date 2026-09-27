# OpenCCman Website

独立的 OpenCCman 产品、隐私与支持网站。简体中文、繁体中文、英文；纯静态 HTML/CSS，无服务端、分析 SDK 或第三方字体。

- Pages 项目：`openccman-website`
- 免费地址：https://openccman-website.pages.dev/
- 正式域名：https://openccman.gewill.org/，已绑定并通过 HTTPS 验证。
- 语言路径：`/zh-Hans/`、`/zh-Hant/`、`/en/`
- 隐私政策：各语言下的 `privacy.html`
- 支持页面：各语言下的 `support.html`

## 本地与部署

```sh
python3 scripts/check.py
python3 -m http.server 8769 --directory site
./deploy.sh
```

只上传 `site/`，不会上传 Git、文档或脚本。部署脚本固定 Wrangler 4.80.0，部署不自动提交或推送。4.132.0 的 `pages project create` 实测改走 Workers，故这里使用经过验证的 Pages CLI 版本。

Cloudflare 静态资源请求免费且不限量；不启用 Functions、数据库或其他付费功能。参阅 [官方计费说明](https://developers.cloudflare.com/pages/functions/pricing/)。

## 配置域名

Cloudflare → Workers & Pages → **openccman-website（Pages）** → Custom domains → Set up a custom domain → `openccman.gewill.org`。遵循向导配置 DNS 和 HTTPS，不仅手工添加 CNAME。

已验证三语主页、隐私及支持页；页面 canonical/alternate 已使用正式域名。博客旧隐私地址保留；App Store Connect 和应用内链接需要单独更新，不随部署自动修改。

## 2.0 产品视频与上线文案

三语首页的功能介绍之后有 25 秒产品视频：`site/assets/motion/openccman-2-<lang>.mp4`（1080p30 H.264 + AAC，每个约 3 MB）和同名 `.jpg` 封面。视频不自动播放；访客点击后才加载，Cloudflare Pages 单文件上限 25 MiB，`scripts/check.py` 会检查。

视频由私有仓库 [gewill/OpenCCman-motion](https://github.com/gewill/OpenCCman-motion) 的 `mux.sh` 生成，界面文字取自 App 的本地化字符串，转换示例用 OpenCC 1.4.2 实际转换过。

三语公开版首页突出 Mac 全局快捷键、原文与结果布局、单文件 TXT 工作流，并移除“即将推出”声明。**公开版不可提前部署**：先确认 iOS 和 macOS 2.0 都在目标 App Store 地区可下载，且 2.0 Pro 价格已按发布计划核对，再合并发布 PR 并运行 `./deploy.sh`。部署后逐一读回三语首页、视频、下载入口、隐私及支持链接。发布前正式站点继续保留预告文案。

本轮桌面 1440×900 与手机 390×844 的简体中文前后截图在 `docs/screenshots/release-2.0/`；对应来源均为本仓库 `main` 的同一页面，本地使用 Python 静态服务器及 Playwright 录制。截图证明网页布局和文案，不证明 App Store 上架或云端部署。

## 验证范围

2026-09-16：本地链接、三语隐私文字与元数据检查；390px/1440px 响应式及深色截图。首页不声称 2.0 已发布，不显示待调整价格。隐私文案来自维护者批准的三语政策。

截图见 `docs/screenshots/`；文字转换图为标注的示例，不是应用运行截图。设计检测器因缺少解析器仅完成降级检查，不能当作完整无障碍审计。
