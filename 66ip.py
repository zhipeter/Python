import requests
import re
import random

def test_ip():
	iplist = []
	html = requests.get("http://www.66ip.cn/areaindex_2/1.html")
	ipn = re.findall(r'<td>高匿代理</td>.*?<tr><td>(.*?)</td><td>(.*?)</td>', html.text, re.S)
	for ip in ipn:
		i = ip[0]+':'+ip[1]
		iplist.append(i.strip())
	print(iplist)

test_ip()