# ArXiv Paper Scraper 📚

一个轻量级的 Python 网页爬虫脚本，用于自动抓取 [ArXiv](https://arxiv.org/) 预印本学术网站上的论文元数据（包括论文标题、作者和摘要内容）。

## 🌟 功能特点
- 自动解析 ArXiv 论文详情页 URL。
- 提取并清理文本数据（Title, Authors, Abstract）。
- 包含基础的请求头伪装（User-Agent）与异常处理。

## 🛠️ 环境依赖
运行此脚本需要安装 Python 3 以及以下第三方库：
```bash
pip install requests beautifulsoup4


 如何使用
1. 下载或克隆本仓库的代码：arxiv_scraper.py。
2. 在代码底部的 test_url 变量中，替换为你想要抓取的 ArXiv 论文链接。
3. 在终端中运行脚本：
Bash
复制代码
python arxiv_scraper.py


⚠️ 免责声明
本项目仅供学术研究和 Python 编程学习交流使用。请对目标服务器保持友好，切勿用于高频并发的恶意抓取。
