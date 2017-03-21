from Download import request
from mongodb_queue import MogoQueue
from bs4 import BeautifulSoup

def start(url):
    response = request.get(url, 3)
    Soup = BeautifulSoup(response.text, 'lxml')
    title = Soup.find('div', class_='gm').find('h1', id='gj').get_text()
    spider_queue = MogoQueue('meinv', 'img_queue')
    spider_queue.clear()
    print(u'清除集合img_queue')
    spider_queue = MogoQueue('meinv', 'img_queue')
    print(u'新建集合img_queue')
    max_span = Soup.find('table', class_='ptt').find_all('td')
    for page in max_span[1:-1]:
        page_url = page.a['href']
        html = request.get(page_url, 3)
        Soup = BeautifulSoup(html.text, 'lxml')
        all_a = Soup.find('div', id='gdt').find_all('a')
        for a in all_a:
            href = a['href']
            name = a.img['alt']
            spider_queue.push(href, title,name)

if __name__ == "__main__":
    start('https://e-hentai.org/g/359468/bfc2e8b566/')