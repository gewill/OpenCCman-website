# OpenCCman Website

独立的 OpenCCman 产品、隐私与支持网站。简体中文、繁体中文、英文；纯静态 HTML/CSS，无服务端、分析 SDK 或第三方字体。

- Pages 项目：`openccman-website`
- 免费地址：https://openccman-website.pages.dev/
- 计划域名：`openccman.gewill.org`，由维护者配置；尚未绑定。
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

绑定成功后，验证三语主页、隐私及支持页，再将页面 canonical/alternate 中的 `https://openccman-website.pages.dev` 更新为正式域名并重新部署。博客旧隐私地址保留；App Store Connect 和应用内链接需要单独更新，不随部署自动修改。

## 验证范围

2026-09-16：本地链接、三语隐私文字与元数据检查；390px/1440px 响应式及深色截图。首页不声称 2.0 已发布，不显示待调整价格。隐私文案来自维护者批准的三语政策。

截图见 `docs/screenshots/`；文字转换图为标注的示例，不是应用运行截图。设计检测器因缺少解析器仅完成降级检查，不能当作完整无障碍审计。
