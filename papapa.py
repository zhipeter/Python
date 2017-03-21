# import urllib.request

# url="http://zhidiao.ml"
# data=urllib.request.urlopen(url).read()
# print(data)


# import urllib.request

# try:
# 	urllib.request.urlopen('http://www.fdsffdsf.cn/')
# 	print("OK")
# except urllib.error.URLError:
# 	print("fuck")


# import http.cookiejar
# import urllib.request

# cookie = http.cookiejar.CookieJar()
# pro = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(pro)
# response=opener.open('https://www.baidu.com')
# for item in cookie:
# 	print("Name="+item.name)
# 	print("Value="+item.value)


import urllib.request
import urllib.parse
 
values={}
values['username'] = "1016903103@qq.com"
values['password']="XXXX"
data = urllib.parse.urlencode(values) 
url = "http://passport.csdn.net/account/login"
geturl = url + "?"+data
print(geturl)
request = urllib.request.Request(geturl)
response = urllib.request.urlopen(request)
print(response.read())