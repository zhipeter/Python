import os
import time
import threading
import multiprocessing
from mongodb_queue import MogoQueue
from Download import request
from bs4 import BeautifulSoup

SLEEP_TIME = 1
lock=threading.Lock()
s='http://www.xiumm.org/'
def E_Hen_crawler(max_threads=5):
    img_queue = MogoQueue('meinv', 'xiumm')
    def pageurl_crawler():
        while True:
            try:
                (url,name) = img_queue.pop()
                print(url)
            except KeyError:
                print('队列没有数据')
                break
            else:
                lock.acquire()
                title = img_queue.pop_title_(url)
                path = str(title).replace('?', '')
                mkdir(path)
                os.chdir('E:\E-Hen\\' + path)
                response = request.get(url, 3)
                response.encoding = 'utf-8'
                Soup = BeautifulSoup(response.text, 'lxml')
                all_url = Soup.find('div', class_='gallary_wrap').find_all('td')
                max_span = Soup.find('div', class_='paginator').find_all('a')
                for td in all_url:
                    href = s + td.img['src']
                    name = td.img['alt'].strip()[-3:]
                    save(href, name)
                for page in max_span:
                    page_url = s + page['href']
                    html = request.get(page_url, 3)
                    Soup = BeautifulSoup(html.text, 'lxml')
                    all_td = Soup.find('div', class_='gallary_wrap').find_all('td')
                    for td2 in all_td:
                        href2 = s + td2.img['src']
                        name2 = td2.img['alt'].strip()[-3:]
                        save(href2, name2)
                img_queue.complete(url)
                lock.release()

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