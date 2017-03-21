from Download import request
from mongodb_queue import MogoQueue
from bs4 import BeautifulSoup


spider_queue = MogoQueue('meinv', 'crawl_queue')
def start(url):
    response = request.get(url, 3)
    Soup = BeautifulSoup(response.text, 'lxml')
    title = Soup.find('div', class_='gm').find('h1', id='gj').get_text()
    max_span = Soup.find('table', class_='ptt').find_all('td')
    i=1
    for page in max_span[1:-1]:
        page_url = page.a['href']
        i += 1
        spider_queue.push(page_url, title)

if __name__ == "__main__":
    start('https://e-hentai.org/g/358581/e6db8cb4b9/')