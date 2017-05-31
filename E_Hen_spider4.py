from Download import request
from mongodb_queue import MogoQueue
from bs4 import BeautifulSoup

spider_queue=MogoQueue('picture','jinji')
def start(url):
    response = request.get(url, 3)
    response.encoding=response.apparent_encoding
    Soup = BeautifulSoup(response.text, 'lxml')
    all_a = Soup.find_all('fieldset', id='info')[1].find_all('a')
    for a in all_a:
        title=a.get_text().strip()
        url='http://www.cartoonmad.com'+a['href']
        print(title,url)
        spider_queue.push(url, title,1)

if __name__ == "__main__":
    start('http://www.cartoonmad.com/comic/1221.html')
