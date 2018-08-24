#-*-coding:utf-8-*-

import urllib2
import re

class Spider(object):
    '''
    内涵段子
    '''
    def load(self,page):
        '''
        :brief 定义一个URL请求
        :param page:需要请求的页数
        :return:返回一个html
        '''

        url = 'https://www.neihan8.com/article/index_'+str(page)+'.html'
        headers = {
            'User-Agent':'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1'
        }
        req = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(req)
        html = response.read()
        # print html
        pattern = re.compile(r'<div.*?class="desc">(.*?)</div>',re.S)
        lists = re.findall(pattern,html)
        return lists

    def printOnePage(self,lists,page):
        '''
        @brief 处理得到的列表
        :param lists:得到的数据
        :param page:页数
        :return:
        '''
        print '-*-*-*-*-第%d页爬取完毕*-*-*-*-*-'%page
        for item in lists:
            self.writeToFile(item)

    def writeToFile(self,text):
        with open('duanzi.txt','a+') as f:
            f.write('-*-*-*-*-*-*-*-*-*-*-*-*-*---*-**-'+'\n')
            f.write(text + '\n')
            f.close()


if __name__ == '__main__':
    myspider = Spider()
    lists = myspider.load(2)
    myspider.printOnePage(lists,2)