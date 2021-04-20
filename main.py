from bsDate import urlList, getBS
from getHtml import getHtml
import threading
import os

#获得种子URL
url = input('Enter a seed address:')
#url等待列表
a = []
#url完成列表
b = []
#状态
zt = 1
#打开写入ULR文件
if not os.path.exists('data'):
    os.mkdir('data')
    os.makedirs('data/htmls')
print(os.getcwd()+'/data/url_a.txt')
fp = open(os.getcwd()+'/data/url_a.txt','wb')
#创建互斥锁
lock = threading.Lock()

#判断有没有http或https
if 'http' not in url or 'https' not in url:
    url = 'http://'+url

#首次取得种子url
a = urlList(getBS(url,'main'),url)

def star(id,url,a):
    # 开始爬取
    while   zt:
        #等待列表不为空就一直取a0
        while len(a) != 0:
            #判断是否已经存在
            if a[0] not in b:
                lis = urlList(getBS(url=a[0],id=id),url=url)
                for l in lis :
                    if l not in b and l not in a:
                        a.append(l)
                        fp.write(a[0].encode('utf-8'))
                    else:
                        print(l,'已经存在！')
                b.append(a[0])
                a.pop(0)

        fp.close()


class myThread(threading.Thread):
    def __init__(self, threadID, url, a):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.url = url
        self.a = a

    def run(self) -> None:
        #线程同步锁
        # lock.acquire()
        star(self.threadID,self.url,a)
        #释放锁
        # lock.release()
class zt(threading.Thread):
    def __init__(self,zt):
        threading.Thread.__init__(self)

    def run(self) -> None:
        zt = input('输入 q 结束！')

#创建线程
thread1 = myThread(1,url,a)
thread2 = myThread(2,url,a)
zt = zt(zt)

#启动
zt.start()
thread1.start()
thread2.start()

#线程结束
thread1.join()
thread2.join()
zt.join()

print('完成！,《ulr_a.txt》和《htmls》文件（夹）存放在',os.getcwd())
