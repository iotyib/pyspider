#-*-coding:utf-8-*-

import urllib2

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
        print html

if __name__ == '__main__':
    myspider = Spider()
    myspider.load(2)