# class Student(object):
	
# 	@property
# 	def score(self):
# 		return self._score

# 	@score.setter
# 	def score(self,value):
# 		if not isinstance(value,int):
# 			raise ValueError('score must be an integer!')
# 		if value<0 or value>100:
# 			raise ValueError('score must between 0 ~ 100!')
# 		self._score=value
		
# s=Student()
# s.score=60
# print(s.score)

#代理设置
import requests
import re
from bs4 import BeautifulSoup
# html = requests.get("http://www.kuaidaili.com/")
# ipn = re.findall(r'<td data-title="IP">(.*?)</td>.*?<td data-title="PORT">(.*?)</td>', html.text, re.S)
# for ip in ipn:
# 	i = ip[0]+':'+ip[1]
# 	print(i)
address='http://www.xiumm.org/photos/TouTiao-17185.html'
response = requests.get(address)
response.encoding='utf-8'
Soup = BeautifulSoup(response.text, 'lxml')
title= Soup.find('div', class_='inline').get_text().strip()
print(title)