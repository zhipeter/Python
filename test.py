# import requests
# import re
# import random
# import time

# class download:

#     def __init__(self):
#         self.iplist = []
#         html = requests.get("http://www.kuaidaili.com/free/")
#         ipn = re.findall(r'<td data-title="IP">(.*?)</td>.*?<td data-title="PORT">(.*?)</td>', html.text, re.S)
#         for ip in ipn:
#             i = ip[0]+':'+ip[1]
#             self.iplist.append(i.strip())

#         self.user_agent_list=[
#             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
#             "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
#             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
#             "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
#             "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
#             "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
#             "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
#             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#             "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#             "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#             "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#             "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#             "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
#             "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
#             "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
#         ]

#     def get(self, url, timeout, proxy=None,num_retries=6):
#         print(u'开始获取：',url)
#         UA=random.choice(self.user_agent_list)
#         headers={'user-Agent':UA,'Connection':'keep-alive','Accept-Encoding':'gzip, deflate'}
        
#         for ip in self.iplist:
#             proxy = {'http': ip}
#             print(u'当前代理是：', proxy)
#             response=requests.get(url, headers=headers, proxies=proxy, timeout=timeout)
#             if response.status_code==200:
#                 print("代理可以")
#             else:
#             	if num_retries > 0:
#             		time.sleep(3)
#             		IP = ''.join(str(random.choice(self.iplist)).strip())
#             		proxy = {'http': IP}
#             		print(u'正在更换代理，10S后将重新获取倒数第', num_retries, u'次')
#             		print(u'当前代理是：', proxy)
#             		return self.get(url, timeout, proxy, num_retries - 1)
#             	else:
#             		print(u'代理也不好使了！取消代理')
#             		return self.get(url, 10)

# request=download()

# html="https://steamcn.com/forum.php"
# request.get(html,10)

# ------------------------------------
# from Download import request
# from bs4 import BeautifulSoup

# def start(url):
#     response = request.get(url, 3)
#     response.encoding=response.apparent_encoding
#     Soup = BeautifulSoup(response.text, 'lxml')
#     all_a = Soup.find_all('fieldset', id='info')[1].find_all('a')
#     all_pages = Soup.find_all('fieldset', id='info')[1].find_all('font')
#     title=0
#     pp=""
#     for page in all_pages:
#         ppp=page.get_text()
#         pp+=(ppp[1:3]+',')
#         print(title,ppp)
#         title+=1
#     print(pp)

# if __name__ == "__main__":
#     start('http://www.cartoonmad.com/comic/1221.html')
# # import os
# path='E:\\E-Hen\\'
# for root,dirs,files in os.walk(path):
#     for dir in dirs:
#         dirpath=path+dir
#         if os.path.exists(dirpath):
#             i=0
#             for root,dirs,files in os.walk(dirpath):
#                 for file in files:
#                     i=i+1
#             print(dir,i)
from Download import request
from bs4 import BeautifulSoup

url='https://www.meitulu.com/t/beautyleg/'
s='http://www.xiumm.org'
# def start(url):
#     response = request.get(url, 3)
#     response.encoding = 'utf-8'
#     Soup = BeautifulSoup(response.text, 'lxml')
#     max_span = Soup.find('div', class_='paginator').find_all('a')
#     i=1
#     page_url = s
#     for page in max_span[0:1]:
#         print(i,"  ",page_url)
#         page_url = s+page['href']
#         html = request.get(page_url, 3)
#         html.encoding='utf-8'
#         Soup = BeautifulSoup(html.text, 'lxml')
#         all_td = Soup.find('div', class_='gallary_wrap').find_all('td')
#         for td in all_td:
#         	address = td.a['href']
#         	title=td.a.img['alt']
#         	print(title)
#         page_url = s + page['href']


# def start(url):
#     response = request.get(url, 3)
#     Soup = BeautifulSoup(response.text, 'lxml')
#     title = Soup.find('div', class_='gm').find('h1', id='gj').get_text()
#     max_span = Soup.find('table', class_='ptt').find_all('td')[-2].get_text()
#     page_url = url
#     for i in range(1,int(max_span)+1):
#     	print(page_url)
#     	page_url =url+'?p='+str(i)
    	
# if __name__ == "__main__":
#     start('https://e-hentai.org/g/436452/62eea14228/')
    def all_url(url):
        html=request.get(url,3)
        html.encoding = html.apparent_encoding
        Soup = BeautifulSoup(html.text, 'lxml')
        all_p = Soup.find('div', class_='boxs').find_all('p', class_='p_title')
        for p in all_p:
            a=p.find('a')
            title=a.get_text()
            self.title=title1
            href=a['href']
            self.url=href

    def html(self,href):
        html=request.get(href,3)
        html_soup = BeautifulSoup(html.text, 'lxml')
        max_span = html_soup.find('div', id='pages').find_all('a')[-2].get_text()
        page_num=1
        self.img(href, max_span, page_num)
        for page in range(1,int(max_span)):
            page_num +=1
            page_url=href+'_'+str(page)
            self.img(page_url,max_span,page_num)

    def img(self,page_url,max_span,page_num):
        img_html=request.get(page_url,3)
        img_soup=BeautifulSoup(img_html.text, 'lxml')
        img_dict=img_soup.find('div', class_='content').find('img')
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