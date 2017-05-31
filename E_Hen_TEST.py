from Download import request
from bs4 import BeautifulSoup
import re

def start(url):
    html = request.get(url, 3)
    html.encoding = html.apparent_encoding
    html_soup = BeautifulSoup(html.text, 'lxml')
    max_span = html_soup.find_all('table')[1].find_all('option')[-1].get_text()[2:4]
    print(max_span)
    for page in range(1, int(max_span) + 1):
        if page < 10:
            page_url = url[:-6] + str(page) + '.html'
        else:
            page_url = url[:-7] + str(page) + '.html'
        page_html = request.get(page_url, 3)
        page_html.encoding = page_html.apparent_encoding
        pattern = re.compile('<a href=".*?"><img src="(.*?)" border="0".*?oncontextmenu=.*?')
        img_url=re.findall(pattern,page_html.text)[0]
        print(img_url)

if __name__ == "__main__":
    start('http://www.cartomad.com/comic/122100072036001.html')