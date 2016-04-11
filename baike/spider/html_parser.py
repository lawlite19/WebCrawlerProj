# coding:UTF8
# 网页转换器
from bs4 import BeautifulSoup
import re
import urlparse
class HtmlParser(object):

    # 获取新的urls
    def _get_new_urls(self, page_url, soup):
        new_urls=set()
        # /view/123.htm
        links = soup.find_all("a", href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url=link["href"]
            # 拼接成完整的url
            new_full_url=urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return  new_urls
    
    # 获取想要的数据，传入url地址和soup对象，
    def _get_new_data(self, page_url, soup):
        res_data={}
        
        #url
        res_data["url"]=page_url
        
        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node=soup.find("dd",class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data["title"]=title_node.get_text()
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node=soup.find("div",class_="lemma-summary")
        res_data["summary"]=summary_node.get_text()
    
        return res_data
    
    
    #传入一个url和下载好的数据，解析出新的url和新的数据，并返回
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup=BeautifulSoup(html_cont,"html.parser",from_encoding="utf-8")
        # 解析得到新的url
        new_urls=self._get_new_urls(page_url,soup)
        # 解析得到新的数据
        new_data=self._get_new_data(page_url,soup)
        return new_urls,new_data

    
    
   
    
    



