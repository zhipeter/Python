from Download import request
from bs4 import BeautifulSoup

def geturl(url):
    try:
        r=request.get(url,3)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print(u'解析url错误')
        return ""

def findtop(demo):
    try:
        soup=BeautifulSoup(demo,"lxml")
        table=soup.find('div',class_="news-text").find('tbody',class_="hidden_zhpm")
        i=0
        for top in table.find_all('div'):
            i += 1
            print(top.get_text())
            if i>20:
                exit()
    except:
        print(u'出错了')

def main():
    url="http://zuihaodaxue.com/zuihaodaxuepaiming2017.html"
    demo=geturl(url)
    findtop(demo)

main()