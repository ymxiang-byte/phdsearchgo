# 博士申请网站系统

这个压缩包包含：

- `index.html`：GitHub Pages 网站首页
- `data/websites.json`：网站数据
- `data/link_status.json`：链接检查结果
- `scripts/check_links.py`：链接检查程序
- `.github/workflows/check-links.yml`：每周一 08:30（新加坡/中国时间）运行
- `phd_application_tracker.xlsx`：申请追踪表

## 一次性部署 GitHub Pages

1. 登录 GitHub，新建一个 **Public** repository，例如 `phd-websites`。
2. 解压本文件，把所有文件和文件夹上传到 repository 根目录。
3. 打开 repository 的 **Settings → Pages**。
4. 在 Build and deployment 中选择 **Deploy from a branch**。
5. Branch 选择 `main`，Folder 选择 `/ (root)`，保存。
6. 发布完成后，固定网址通常是：
   `https://你的GitHub用户名.github.io/phd-websites/`

以后更新 `data/websites.json` 或 `index.html`，同一个网址会自动显示新版。

## 申请追踪

把 `phd_application_tracker.xlsx` 上传到 Google Drive，然后选择：
**Open with → Google Sheets**，即可跨设备同步使用。

建议：
- 每发现一个项目，立即录入截止日期和官方链接。
- A 级项目每周更新一次。
- 每行必须填写“下一步行动”和“下次跟进日期”。
- 不再申请的项目不要删除，改成“放弃”并写明原因。
