import urllib.request
import urllib.parse
import re
 
page = 3
url = 'http://www.qiushibaike.com/hot/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('h2>(.*?)</h2.*?content">(.*?)</.*?number">(.*?)</',re.S)
    items = re.findall(pattern,content)
    for item in items:
        print(item[0].strip(),item[1].strip(),item[2].strip())
except urllib.request.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)