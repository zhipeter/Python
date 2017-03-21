import re
import http.cookiejar
import urllib.request
import urllib.parse
 
def getXSRF(data):
    cer = re.compile('name="_xsrf" value="(.*)"', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]
 
def getOpener(head):
    # deal with the Cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener
 
header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Host': 'http://4m3.tongji.edu.cn/eams/login.action',
    'DNT': '1'
}
 
url = 'http://www.tongji-pe.tongji.edu.cn/webscore/search/websearch.aspx'
opener = getOpener(header)
op = opener.open(url)
data = op.read()

url='http://www.tongji-pe.tongji.edu.cn/webscore/search/websearch.aspx'
id = '1450856'
password = '1450856'
postDict = {
        'txt_stid': id,
        'txt_pwd': password,
}
postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url, postData)
data = op.read()
 
print(data.decode())



