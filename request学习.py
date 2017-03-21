from Download import request
import re

def getHTML(url):
    try:
        r=request.get(url,3)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(itl,html):
    try:
        plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price=eval(plt[i].split(':')[1])
            title=eval(tlt[i].split(':')[1])
            itl.append([price,title])
    except:
        print("")

def printGoods(itl):
    tplt="{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count=0
    for g in itl:
        count+=1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods="电脑"
    depth=3
    start_url='http://s.taobao.com/search?q='+goods
    infoList=[]
    for i in range(depth):
        try:
            url=start_url+'&s='+str(44*i)
            html=getHTML(url)
            parsePage(infoList,html)
        except:
            continue
    printGoods(infoList)

main()