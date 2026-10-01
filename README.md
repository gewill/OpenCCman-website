# OpenCCman Website

独立的 OpenCCman 产品、隐私与支持网站。简体中文、繁体中文、英文；静态 HTML/CSS 加少量同源脚本，无服务端、分析 SDK、第三方字体或第三方脚本。视觉系统是「稿纸与校样」，规则见 `DESIGN.md`。

- Pages 项目：`openccman-website`
- 免费地址：https://openccman-website.pages.dev/
- 正式域名：https://openccman.gewill.org/，已绑定并通过 HTTPS 验证。
- 语言路径：`/zh-Hans/`、`/zh-Hant/`、`/en/`
- 隐私政策：各语言下的 `privacy.html`
- 支持页面：各语言下的 `support.html`
- 更新记录：各语言下的 `changelog.html`，按应用仓库 `CHANGELOG.md` 提炼；未发布版本明确标为候选。
- 使用指南：各语言下的 `guides/` 目录页与五篇独立文章，介绍入门转换、地区预设、UTF-8 TXT、Mac 选中文字快捷键及 OpenCC 原始项目。应用操作指南只承诺已公开的 2.0 能力；上游介绍另行区分项目能力与 App 功能。

## 本地与部署

```sh
python3 scripts/build_site.py
python3 scripts/check.py
python3 -m http.server 8769 --directory site
./deploy.sh
```

所有页面、`sitemap.xml` 和 `site/assets/specimens.js` 都由 `python3 scripts/build_site.py` 生成：指南的三语正文在 `scripts/guide_content.py`，首页、更新记录、支持、隐私、404 和语言选择页的三语文案在 `scripts/site_content.py`。改完文案先生成，再运行 `scripts/check.py`；检查会拒绝未同步的生成页、失效站内链接、内联样式或脚本（CSP 只允许同源资源）以及缺字的字体子集。指南结构参考 [iPerfman Guides](https://iperfman.com/en/guides/) 的目录、独立问题页和步骤式说明，文案与功能边界按 OpenCCman 已发布版单独核实。

首页校样台和预设指南对照表里的转换示例来自 `scripts/specimens.json`，由 `python3 scripts/specimens.py` 调用 OpenCC 1.4.2（App 内置版本）生成，并逐句核对整句输出。App 的四个预设对应 OpenCC 的 `t2s`、`s2t`、`s2twp`、`s2hk`。装有 OpenCC 1.4.2 时 `check.py` 会重算比对，否则打印 SKIP。

`site/assets/fonts/` 里是 Noto Serif SC/TC 与霞鹜文楷按用字做的子集，已改名为 OpenCCman Serif SC/TC、OpenCCman Hand，许可见同目录 `OFL.txt`。标题、结果行或手写批注出现新字时，`check.py` 会提示；用装有 fonttools 和 brotli 的 Python 运行 `python3 scripts/fonts.py --serif-sc NotoSerifSC[wght].ttf --serif-tc NotoSerifTC[wght].ttf --hand LXGWWenKai-Regular.ttf` 重做子集，源字体下载地址写在脚本开头。

只上传 `site/`，不会上传 Git、文档或脚本。部署脚本固定 Wrangler 4.80.0，部署不自动提交或推送。4.132.0 的 `pages project create` 实测改走 Workers，故这里使用经过验证的 Pages CLI 版本。

Cloudflare 静态资源请求免费且不限量；不启用 Functions、数据库或其他付费功能。参阅 [官方计费说明](https://developers.cloudflare.com/pages/functions/pricing/)。

## 配置域名

Cloudflare → Workers & Pages → **openccman-website（Pages）** → Custom domains → Set up a custom domain → `openccman.gewill.org`。遵循向导配置 DNS 和 HTTPS，不仅手工添加 CNAME。

已验证三语主页、更新记录、隐私及支持页；页面 canonical/alternate 已使用正式域名。博客旧隐私地址保留；App Store Connect 和应用内链接需要单独更新，不随部署自动修改。

## 2.0 产品视频与上线文案

三语首页的功能介绍之后有 25 秒产品视频：`site/assets/motion/openccman-2-<lang>.mp4`（1080p30 H.264 + AAC，每个约 3 MB）和同名 `.jpg` 封面。视频不自动播放；访客点击后才加载，Cloudflare Pages 单文件上限 25 MiB，`scripts/check.py` 会检查。

视频由私有仓库 [gewill/OpenCCman-motion](https://github.com/gewill/OpenCCman-motion) 的 `mux.sh` 生成，界面文字取自 App 的本地化字符串，转换示例用 OpenCC 1.4.2 实际转换过。

三语公开版首页突出 Mac 全局快捷键、原文与结果布局、单文件 TXT 工作流。2.0 已公开发布，正式站点已部署并读回三语首页、视频、下载入口、隐私及支持链接。更新记录列出公开版 2.0；2.1 更新记录按 2026-10-01 发布内容更新，注明 Mac Pro 1 GiB、移动端 10 MiB 和 Shortcuts 系统要求。

本轮桌面 1440×900 与手机 390×844 的简体中文前后截图在 `docs/screenshots/release-2.0/`；对应来源均为本仓库 `main` 的同一页面，本地使用 Python 静态服务器及 Playwright 录制。截图证明网页布局和文案，不证明 App Store 上架或云端部署。

## 验证范围

2026-09-16：本地链接、三语隐私文字与元数据检查；390px/1440px 响应式及深色截图。隐私文案来自维护者批准的三语政策。

2026-09-29：三语更新记录部署并从正式域名读回；2.0 标为已发布，2.1 保留候选状态。此项验证不代表 2.1 已获 App Review 批准或公开上架。

2026-09-29：稿纸与校样改版。本地用带 `_headers` 同款 CSP 的静态服务器验证三语页面无拦截、交互可用；桌面 1440、手机 390 与深色截图附在对应 PR 中，不存入仓库。

截图见 `docs/screenshots/`；文字转换图为标注的示例，不是应用运行截图。设计检测器因缺少解析器仅完成降级检查，不能当作完整无障碍审计。
