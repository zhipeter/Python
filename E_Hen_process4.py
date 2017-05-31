import os
import time
import threading
import multiprocessing
from mongodb_queue import MogoQueue
from Download import request
from bs4 import BeautifulSoup
import re

SLEEP_TIME = 1
lock=threading.Lock()
def E_Hen_crawler(max_threads=4):
    jinji = MogoQueue('meinv', 'jinji')
    def pageurl_crawler():
        while True:
            try:
                (url,name) = jinji.pop()
                print(url)
            except KeyError:
                print('队列没有数据')
                break
            else:
                lock.acquire()
                img_urls=[]
                html = request.get(url, 10)
                title = jinji.pop_title_(url)
                mkdir(title)
                os.chdir('E:\E-Hen\\' + title)
                html.encoding = html.apparent_encoding
                html_soup = BeautifulSoup(html.text, 'lxml')
                max_span = html_soup.find_all('table')[1].find_all('option')[-1].get_text()[2:4]
                for page in range(1,int(max_span)+1):
                    if page < 10:
                        page_url=url[:-6]+str(page)+'.html'
                    else:
                        page_url = url[:-7] + str(page) + '.html'
                    page_html = request.get(page_url, 10)
                    page_html.encoding = page_html.apparent_encoding
                    pattern = re.compile('<a href=".*?"><img src="(.*?)" border="0".*?oncontextmenu=.*?')
                    img_url = re.findall(pattern, page_html.text)[0]
                    img_urls.append(img_url)
                    print(u'得到图片的链接')
                    save(img_url)
                jinji.complete(url)
                lock.release()

    def save(img_url):
        name=img_url[-7:]
        print(u'开始保存：', img_url,'\n')
        img=request.get(img_url,15)
        f=open(name,'ab')
        f.write(img.content)
        f.close()

    def mkdir(path):
        path = path.strip()
        isExists = os.path.exists(os.path.join("E:\E-Hen", path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join("E:\E-Hen", path))
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False

    threads = []
    while threads or jinji:
        for thread in threads:
            if not thread.is_alive(): ##is_alive是判断是否为空,不是空则在队列中删掉
                threads.remove(thread)
        while len(threads) < max_threads and jinji.peek(): ##线程池中的线程少于max_threads 或者 crawl_qeue时
            thread = threading.Thread(target=pageurl_crawler) ##创建线程
            thread.setDaemon(True) ##设置守护线程
            thread.start() ##启动线程
            threads.append(thread) ##添加进线程队列
        time.sleep(SLEEP_TIME)

def process_crawler():
    process = []
    num_cpus = multiprocessing.cpu_count()
    print('将会启动进程数为：', num_cpus)
    for i in range(num_cpus):
        p = multiprocessing.Process(target=E_Hen_crawler) ##创建进程
        p.start() ##启动进程
        process.append(p) ##添加进进程队列
    for p in process:
        p.join() ##等待进程队列里面的进程结束

if __name__ == "__main__":
    process_crawler()