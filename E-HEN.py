from bs4 import BeautifulSoup
import os
from Download import request

class E_Hen():

    def all_url(self,url):
        html=request.get(url,3)
        Soup = BeautifulSoup(html.text, 'lxml')
        title =Soup.find('div',class_='gm').find('h1',id='gj').get_text()
        path = str(title).replace("?", "_")
        self.mkdir(path)
        os.chdir("E:\E-Hen\\" + path)
        max_span = Soup.find('table', class_='ptt').find_all('td')
        i=1
        for page in max_span[1:-1]:
            page_url=page.a['href']
            print("获取第" + str(i) + "页")
            i+=1
            self.html(page_url)

    def html(self,page_url):
        html = request.get(page_url, 3)
        Soup = BeautifulSoup(html.text, 'lxml')
        all_a = Soup.find('div', id='gdt').find_all('a')
        for a in all_a:
            href = a['href']
            name = a.img['alt']
            self.img(href, name)

    def img(self,href,name):
        page_name=name
        html=request.get(href,3)
        html_soup = BeautifulSoup(html.text, 'lxml')
        img=html_soup.find('div',id='i3').find('img')
        img_url=img['src']
        print(u'得到图片的链接')
        self.save(img_url,page_name)

    def save(self,img_url,page_name):
        name=page_name
        print(u'开始保存：', img_url,'\n')
        img=request.get(img_url,3)
        f=open(name+'.jpg','ab')
        f.write(img.content)
        f.close()

    def mkdir(self,path):
        path=path.strip()
        isExits=os.path.exists(os.path.join("E:\E-Hen",path))
        if not isExits:
            print(u'建立了一个名字叫做', path, u'的文件夹')
            os.makedirs(os.path.join("E:\E-Hen",path))
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在')
            return False

M=E_Hen()
M.all_url('https://e-hentai.org/g/671126/fc67df3620/')