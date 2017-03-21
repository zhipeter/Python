import os
import time
import threading
import multiprocessing
from mongodb_queue import MogoQueue
from Download import request
from bs4 import BeautifulSoup

SLEEP_TIME = 1

def E_Hen_crawler(max_threads=5):
    crawl_queue = MogoQueue('meinv', 'crawl_queue') ##这个是我们获取URL的队列
    img_queue = MogoQueue('meinv', 'img_queue')
    def pageurl_crawler():
        while True:
            try:
                url = crawl_queue.pop()
                print(url)
            except KeyError:
                print('队列没有数据')
                break
            else:
                title = crawl_queue.pop_title(url)
                path = str(title).replace('?', '') ##测试过程中发现一个标题有问号
                mkdir(path)
                os.chdir('E:\Cover\\' + path)
                html = request.get(url, 3)
                Soup = BeautifulSoup(html.text, 'lxml')
                all_a = Soup.find('div', id='gdt').find_all('a')
                for a in all_a:
                    href = a['href']
                    name = a.img['alt']
                    html = request.get(href, 3)
                    html_soup = BeautifulSoup(html.text, 'lxml')
                    img = html_soup.find('div', id='i3').find('img')
                    img_url = img['src']
                    img_queue.push_imgurl(title,img_url)
                    print(u'得到图片的链接')
                    save(img_url, name)
                    img_queue.complete(img_url)
                crawl_queue.complete(url)

    def save(img_url,page_name):
        name=page_name
        print(u'开始保存：', img_url,'\n')
        img=request.get(img_url,3)
        f=open(name+'.jpg','ab')
        f.write(img.content)
        f.close()

    def mkdir(path):
        path = path.strip()
        isExists = os.path.exists(os.path.join("E:\Cover", path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join("E:\Cover", path))
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False

    threads = []
    while threads or crawl_queue:
        """
        这儿crawl_queue用上了，就是我们__bool__函数的作用，为真则代表我们MongoDB队列里面还有数据
        threads 或者 crawl_queue为真都代表我们还没下载完成，程序就会继续执行
        """
        for thread in threads:
            if not thread.is_alive(): ##is_alive是判断是否为空,不是空则在队列中删掉
                threads.remove(thread)
        while len(threads) < max_threads and crawl_queue.peek(): ##线程池中的线程少于max_threads 或者 crawl_qeue时
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