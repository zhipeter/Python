from bs4 import BeautifulSoup
import os
from Download import request
from pymongo import MongoClient
import datetime
import re

class mzitu():

    def __init__(self):
        client=MongoClient()
        db=client['meinv']
        self.meizitu_collection=db['meizitu']
        self.title=''
        self.url=''
        self.img_urls=[]

    def all_url(self,url):
        html=request.get(url,3)
        Soup = BeautifulSoup(html.text, 'lxml')
        all_a = Soup.find('div', class_='all').find_all('a')
        for a in all_a:
            title=a.get_text()
            self.title=title
            print(u'开始保存：',title)
            path=str(title).replace("?","_")
            self.mkdir(path)
            os.chdir("E:\mzitu\\"+path)
            href=a['href']
            self.url=href
            if self.meizitu_collection.find_one({'主题页面':href}):
                print(u'这个页面已经爬取过了')
            else:
                self.html(href)

    def html(self,href):
        html=request.get(href,3)
        html_soup = BeautifulSoup(html.text, 'lxml')
        max_span = html_soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()
        page_num=0
        for page in range(1,int(max_span)+1):
            page_num +=1
            page_url=href+'/'+str(page)
            self.img(page_url,max_span,page_num)

    def img(self,page_url,max_span,page_num):
        img_html=request.get(page_url,3)
        img_soup=BeautifulSoup(img_html.text, 'lxml')
        img_dict=img_soup.find('div', class_='main-image').find('img')
        if img_dict is not None:
            img_url=img_dict['src']
        else:
            print(u'没有获取到img_url')
            return None
        img_url_reg=re.compile('http://.*?\.jpg', re.S)
        if re.match(img_url_reg, img_url):
            self.img_urls.append(img_url)
            if int(max_span) == page_num:
                self.save(img_url)
                post = {
                    '标题': self.title,
                    '主题页面': self.url,
                    '图片地址': self.img_urls,
                    '获取时间': datetime.datetime.now()
                }
                self.meizitu_collection.save(post)
                print(u'插入数据库成功')
            else:
                self.save(img_url)
        else:
            print(u'图片不是有效链接！')

    def save(self,img_url):
        name=img_url[-9:-4]
        name=re.sub(r'/', '-', name)
        print(u'开始保存：', img_url)
        img=request.get(img_url,3)
        f=open(name+'.jpg','ab')
        f.write(img.content)
        f.close()

    def mkdir(self,path):
        path=path.strip()
        isExits=os.path.exists(os.path.join("E:\mzitu",path))
        if not isExits:
            print(u'建立了一个名字叫做', path, u'的文件夹')
            os.makedirs(os.path.join("E:\mzitu",path))
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在')
            return False

M=mzitu()
M.all_url('http://www.mzitu.com/all')