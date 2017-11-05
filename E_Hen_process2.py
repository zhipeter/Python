import os
import time
import threading
import multiprocessing
from mongodb_queue import MogoQueue
from Download import request
from bs4 import BeautifulSoup

SLEEP_TIME = 1

def E_Hen_crawler(max_threads=5):
    img_queue = MogoQueue('meinv', 'img_queue')
    def pageurl_crawler():
        while True:
            try:
                (url,name) = img_queue.pop()
                print(url)
            except KeyError:
                print('队列没有数据')
                break
            else:
                title = img_queue.pop_title_(url)
                path = str(title).replace('?', '')
                mkdir(path)
                os.chdir('E:\E-Hen\\' + path)
                html = request.get(url, 3)
                html_soup = BeautifulSoup(html.text, 'lxml')
                img = html_soup.find('div', id='i3').find('img')
                img_url = img['src']
                print(u'得到图片的链接')
                save(img_url, name)
                img_queue.complete(url)

    def save(img_url,page_name):
        name=page_name
        print(u'开始保存：', img_url,'\n')
        img=request.get(img_url,15)
        f=open(name+'.jpg','ab')
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
    while threads or img_queue:
        for thread in threads:
            if not thread.is_alive(): ##is_alive是判断是否为空,不是空则在队列中删掉
                threads.remove(thread)
        while len(threads) < max_threads and img_queue.peek(): ##线程池中的线程少于max_threads 或者 crawl_qeue时
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