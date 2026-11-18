# 部署说明

本仓库每天自动从两处收集内容并生成 README.md（收录页面）：
- **论文**：arXiv 关键词检索，结果存入 `data/papers.json`。
- **GitHub 项目**：GitHub 仓库搜索（名称或简介需同时含 agent 相关词与明确的防护术语，且至少 3 ⭐），结果存入 `data/github_repos.json`。

## 部署
1. 在 GitHub 新建仓库，把本文件夹内容全部上传。
2. Settings → Actions → General → Workflow permissions，选 **Read and write permissions**，保存。（不做这一步，自动提交会失败。）
3. Actions 页签 → update-papers → **Run workflow** 手动运行一次。之后每天自动运行。
4. 仓库首页显示的 README.md 就是收录页面。

## 维护
- 加入论文：编辑 `data/seed_papers.json`（字段：id、title、category、note，可选 verify）。
- 剔除论文或项目：把 arXiv ID 或 `owner/repo` 加入 `data/exclude.json`。
- 调整项目的最低 Star 数或检索词：修改 `scripts/update_papers.py` 中的 `GH_MIN_STARS`、`GITHUB_QUERIES`。
- 本地运行：`python scripts/update_papers.py`（只需 Python 3，无第三方依赖）。

## 已知局限
- 自动收录是关键词匹配，会有误收。第一次运行后建议花几分钟把明显跑题的项目加入 `exclude.json`。
- GitHub 只收录在名称或简介中明确提到相关术语的仓库。
- arXiv 只覆盖 arXiv 上的论文，不含仅在会议官网或 ACL Anthology 发表的工作。
