# import requests
# import re
# import random
# import time

# class download:

#     def __init__(self):
#         self.iplist = []
#         html = requests.get("http://www.kuaidaili.com/")
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

# html="http://www.baidu.com"
# request.get(html,10)

# ------------------------------------
from Download import request
from bs4 import BeautifulSoup

def start(url):
    response = request.get(url, 3)
    response.encoding=response.apparent_encoding
    Soup = BeautifulSoup(response.text, 'lxml')
    all_a = Soup.find_all('fieldset', id='info')[1].find_all('a')
    all_pages = Soup.find_all('fieldset', id='info')[1].find_all('font')
    title=0
    pp=""
    for page in all_pages:
        ppp=page.get_text()
        pp+=(ppp[1:3]+',')
        print(title,ppp)
        title+=1
    print(pp)

if __name__ == "__main__":
    start('http://www.cartoonmad.com/comic/1221.html')
# import os
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
