import requests
from bs4 import BeautifulSoup
import time

class ArxivScraper:
    """
    一个简单的 ArXiv 学术论文信息抓取工具。
    用于提取指定 ArXiv 论文链接的标题、作者和摘要内容。
    """
    
    def __init__(self):
        # 设置请求头，模拟真实浏览器访问，避免被服务器误判为恶意脚本
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9'
        }

    def fetch_paper_info(self, url):
        """
        抓取并解析论文信息
        :param url: ArXiv 论文详情页 URL (例如: https://arxiv.org/abs/xxxx.xxxxx)
        :return: 包含标题、作者和摘要的字典
        """
        print(f"[*] 正在请求页面: {url}")
        
        try:
            # 发起 GET 请求
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status() # 如果状态码不是 200，将引发异常
            
            # 使用 BeautifulSoup 解析 HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 1. 提取标题
            title_tag = soup.find('h1', class_='title')
            title = title_tag.text.replace('Title:', '').strip() if title_tag else '未找到标题'
            
            # 2. 提取作者
            authors_tag = soup.find('div', class_='authors')
            authors = authors_tag.text.replace('Authors:', '').strip() if authors_tag else '未找到作者'
            
            # 3. 提取摘要
            abstract_tag = soup.find('blockquote', class_='abstract')
            abstract = abstract_tag.text.replace('Abstract:', '').strip() if abstract_tag else '未找到摘要'
            
            return {
                'url': url,
                'title': title,
                'authors': authors,
                'abstract': abstract
            }
            
        except requests.exceptions.RequestException as e:
            print(f"[!] 网络请求失败: {e}")
            return None
        except Exception as e:
            print(f"[!] 解析页面时发生错误: {e}")
            return None

if __name__ == "__main__":
    # 实例化爬虫对象
    scraper = ArxivScraper()
    
    # 测试链接（这里以一篇经典的 AI 论文为例，你也可以换成博弈论或经济学相关的论文链接）
    test_url = "https://arxiv.org/abs/1706.03762" 
    
    # 为了对服务器友好，建议在批量抓取时加入延时
    time.sleep(1) 
    
    result = scraper.fetch_paper_info(test_url)
    
    if result:
        print("\n" + "="*50)
        print(f"【论文标题】\n{result['title']}\n")
        print(f"【作者】\n{result['authors']}\n")
        print(f"【摘要】\n{result['abstract']}")
        print("="*50 + "\n")
