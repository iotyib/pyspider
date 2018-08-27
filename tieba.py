import urllib2
import urllib

def tiebaSpider(url,beginPage,endPage):
    for page in range(beginPage,endPage):
        pn = (page - 1)*50
        filename = "第"+str(page)+"页.html"
        fullurl = url + "&pn=" + str(pn)
        html = loadPage(fullurl,filename)
        writeFile(html,filename)

def loadPage(url,filename):
    print "正在下载......"+filename
    headers = {
        "User-Agent" : "Mozilla/5.0(compatible;MSIE9.0;Windows NT 6.1; Trident/5.0;)"
    }
    request = urllib2.request(url,headers=headers)
    response = urllib2.urlopen(request)
    return  response.read()

def writeFile(html,filename):
    print '正在存储......'+filename
    with open(filename,'w') as f:
        f.write(html)
    print'-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-'

if __name__ == '__main__':
    kw = raw_input("请输入需要爬取的贴吧:")
    beginPage = int(raw_input("请输入起始页码"))
    endPage = int(raw_input("请输入终止页"))

    url = "http://www.tieba.baidu.com/f?"
    key = urllib.urlencode("kw":kw)

    url = url + key
    tiebaSpider(url,beginPage,endPage)
