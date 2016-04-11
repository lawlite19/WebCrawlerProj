# coding:UTF8


class UrlManage(object):
    
    # 构造函数，定义两个集合对象
    def __init__(self):
        self.new_urls=set()
        self.old_urls=set()
    
    #添加一个url
    def add_new_url(self,url):
        if url is None:
            return
        # 当前url不在新的urls集合中也不在旧的urls集合中，将添加到新的urls集合中
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
        
    #添加所有的urls
    def add_new_urls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)
    
    #判断是否有新url
    def has_new_url(self):
        return len(self.new_urls)!=0

    #获得新的url
    def get_new_url(self):
        new_url=self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    

    
    
    
    
    
    
    
    

    
    



