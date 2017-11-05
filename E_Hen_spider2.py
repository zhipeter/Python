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
    start('https://e-hentai.org/g/634810/be7f15e14a/')
    # "https://e-hentai.org/g/217371/bf72e21e08/"
    # "https://e-hentai.org/g/39687/e7538d3165/"
    # "https://e-hentai.org/g/217401/4a28472869/"
    # "https://e-hentai.org/g/217406/152ee08fbf/"
    # "https://e-hentai.org/g/217437/d230898d3f/"
    # "https://e-hentai.org/g/78413/36722d2f24/"

    #'https://e-hentai.org/g/164662/366da26540/'
    #'https://e-hentai.org/g/155912/ab27b7ac21/'
    #'https://e-hentai.org/g/781050/4722d8efa9/'
    #BUG 'https://e-hentai.org/g/436452/62eea14228/'
    #'https://e-hentai.org/g/446994/ac99503e8a/'
    #'https://e-hentai.org/g/494637/5aafc8cc53/'
    #'https://e-hentai.org/g/490628/796d318869/'
    #'https://e-hentai.org/g/528354/ebdb3157e8/'
    #'https://e-hentai.org/g/526651/3c49e354f1/'
    #'https://e-hentai.org/g/522209/746b957e8f/'
    #'https://e-hentai.org/g/510860/dee7dfb926/'
    #'https://e-hentai.org/g/536174/6a9f6dc9f1/'

    #'https://e-hentai.org/g/781050/4722d8efa9/'
    #'https://e-hentai.org/g/774622/0b807faca1/'
    #'https://e-hentai.org/g/774627/356de3a839/'
    #'https://e-hentai.org/g/771827/622d9a68a6/'
    #'https://e-hentai.org/g/762385/aa47c04d45/'
    #'https://e-hentai.org/g/755993/adfcb0ff5a/'
    #'https://e-hentai.org/g/757237/80812b5985/'
    #'https://e-hentai.org/g/757238/032479cf3b/'
    #'https://e-hentai.org/g/754384/cab885727c/'
    #'https://e-hentai.org/g/754058/de307d612a/'
    #'https://e-hentai.org/g/750797/3645c3cfdb/'
    #'https://e-hentai.org/g/751600/65f8056f4e/'
    #'https://e-hentai.org/g/750016/b0d76680b2/'
    #'https://e-hentai.org/g/747920/196e4af0d1/'

    #‘https://e-hentai.org/g/890669/1bd0595181/’
    #‘https://e-hentai.org/g/892639/7fa244c0d4/’
