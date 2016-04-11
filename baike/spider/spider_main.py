# coding:UTF8
# 爬虫总调度程序
from baike.spider import html_downloader, html_parser, url_manager,\
    html_outputer

class SpiderMain(object):
    #构造函数 初始化对象
    def __init__(self):
        # urls对象，为url_manager模块的UrlManage类
        self.urls=url_manager.UrlManage()
        # downloader对象，为html_downloader模块的HtmlDownloader类
        self.downloader=html_downloader.HtmlDownloader()
        # parse对象，为html_parser模块下的HtmlParser类
        self.parser=html_parser.HtmlParser()
        # outputer对象，为html_outputer模块下的HtmlOutPuter类
        self.outputer=html_outputer.HtmlOutPuter()
    #爬取函数，参数为当前对象，和根url地址
    def craw(self,root_url):
        count=1
        #urls对象的add_new_url方法，将url添加到待爬取的url
        self.urls.add_new_url(root_url)
        # 遍历urls对象
        while self.urls.has_new_url():
            try:
                # 获得新的url
                new_url = self.urls.get_new_url()
                # 打印爬取的个数和url地址
                print 'craw %d:%s' % (count, new_url)
                # 通过url地址获得网页的内容
                html_cont = self.downloader.download(new_url)
                # 交给解析器去解析网页的内容，并且返回解析到的新的urls,和筛选的网页数据
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 将解析获得的urls放到将当前对象的urls对象中
                self.urls.add_new_urls(new_urls)
                # 输出对象收集数据
                self.outputer.collect_data(new_data)
                
                #爬取指定数量就跳出
                if count == 10:
                    break
                count = count + 1
            except:
                print 'craw failed'
                
        
        # 网页输出器，输出到文件中
        self.outputer.out_html();
        
        
if __name__=="__main__":
    print '开始爬虫'
    #指定爬取的根url
    root_url="http://baike.baidu.com/view/21087.htm"
    obj_spider=SpiderMain()
    # 调用爬虫方法
    obj_spider.craw(root_url)
