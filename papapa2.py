import urllib.request
import urllib.parse
import re
import http.cookiejar

class TJ:

	def __init__(self):
		self.loginUrl = 'http://www.tongji-pe.tongji.edu.cn/webscore/Default.aspx'
		self.cookies = http.cookiejar.MozillaCookieJar()
		self.postdata=urllib.parse.urlencode({
			'txt_stid':'1450856',
			'txt_pwd':'1450856'
			}).encode()
		self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cookies))

	def getPage(self):
		header = {
		'Accept-Encoding':'gzip, deflate',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
		}
		request  = urllib.request.Request(
			url=self.loginUrl,
			data=self.postdata,
			headers=header)
		result = self.opener.open(request)
		data=result.read()
		print(data.decode())

tj=TJ()
tj.getPage()
