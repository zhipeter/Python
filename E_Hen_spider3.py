from Download import request
from mongodb_queue import MogoQueue
from bs4 import BeautifulSoup

spider_queue = MogoQueue('meinv', 'xiumm')
spider_queue.clear()
print(u'清除集合xiumm')
spider_queue = MogoQueue('meinv', 'xiumm')
print(u'新建集合xiumm')
s='http://www.xiumm.org/'

def start(url):
    response = request.get(url, 3)
    Soup = BeautifulSoup(response.text, 'lxml')

    max_span = Soup.find('div', class_='paginator').find_all('a')
    for page in max_span[0:1]:
        page_url = s+page['href']
        html = request.get(page_url, 3)
        Soup = BeautifulSoup(html.text, 'lxml')
        all_td = Soup.find('div', class_='gallary_wrap').find_all('td')
        for td in all_td:
            address = td.a['href']
            get_url(address)

def get_url(address):
    response = request.get(address, 3)
    response.encoding = 'utf-8'
    Soup = BeautifulSoup(response.text, 'lxml')
    title = Soup.find('div', class_='inline').get_text().strip()
    all_url = Soup.find('div', class_='gallary_wrap').find_all('td')
    max_span = Soup.find('div', class_='paginator').find_all('a')
    for td in all_url:
        href = s + td.img['src']
        name = td.img['alt'].strip()[-3:]
        spider_queue.push(href, title, name)
    for page in max_span:
        page_url = s + page['href']
        html = request.get(page_url, 3)
        Soup = BeautifulSoup(html.text, 'lxml')
        all_td = Soup.find('div', class_='gallary_wrap').find_all('td')
        for td2 in all_td:
            href2 = s + td2.img['src']
            name2 = td2.img['alt'].strip()[-3:]
            spider_queue.push(href2, title, name2)

if __name__ == "__main__":
    start('http://www.xiumm.org/')