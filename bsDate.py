from bs4 import BeautifulSoup
from getHtml import getHtml

#分析bs

#取链接
def urlList(soup,url):
    #一个url列表
    list = []

    #找到所有链接
    a = soup.find_all('a');
    for item in a:
        itemUrl = str(item.get('href'))
        if itemUrl == '/':
            itemUrl = url +'/'
        if 'http' not in itemUrl and itemUrl !='/':
            itemUrl = url + '/' + itemUrl

        if itemUrl not in list :
            list.append(itemUrl)

    return list




#获得bs
def getBS(url,id=None):
        #创建BS对象
        soup = BeautifulSoup(getHtml(url,id),features="html.parser")
        return soup