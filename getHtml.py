import re
import time
import os
import urllib3

#获得url内容
def getHtml(url,id=None):
    # url为空时直接返回问题url
    if True:
        try:
            if not os.path.exists('data/htmls'):
                os.makedirs('data/htmls')
            #获取时间
            t = time.asctime(time.localtime(time.time()))
            #创建文件
            name = re.sub(r':*/*\.*\?*&*=*','',url)
            # print(os.getcwd()+'/data/htmls/'+name)
            fp = open(os.getcwd()+'/data/htmls/'+name+'.html','wb+')
            #设置请求头
            header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"
            }
            #显示读取的链接
            print('[',t,'] [线程：',id,"]正在读取：",url)
            #创建请求
            http = urllib3.PoolManager()
            #接收返回的请求
            response = http.request(method="GET",url=url,fields=None,headers=header)
            #接收返回内容
            try:
                html = response.data.decode('utf-8') # 注意, 返回的是字节数据.需要转码.
                fp.write(html.encode('utf-8'))
            except:
                html = response.data
                fp.write(html)

            fp.close()

            return html
        except:
            print('error!')
            return "error!"
