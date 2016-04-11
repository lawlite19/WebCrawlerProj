# coding:UTF8
# 网页输出器

class HtmlOutPuter(object):

    def __init__(self):
        #构造函数定义datas属性，
        self.datas=[]
    
    # 收集数据
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    # 输出到文件中
    def out_html(self):
        fout=open('output.html','w')
        fout.write("<html>")
        fout.write("<head>")
        fout.write('<meta charset="utf-8"></meta>')
        fout.write("<title>百度百科Python页面爬取相关数据</title>")
        fout.write("</head>")
        fout.write("<body>")
        fout.write('<h1 style="text-align:center">在百度百科中爬取相关数据展示</h1>')
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data["url"])
            fout.write("<td><a href='%s'>%s</a></td>" % (data["url"].encode("utf-8"),data["title"].encode("utf-8")))
            fout.write("<td>%s</td>" % data["summary"].encode("utf-8"))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        
        
    
    
    
    

    
    



