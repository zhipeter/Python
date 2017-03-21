import re
import requests

iplist=[]
html=requests.get("http://haoip.cc/tiqu.htm")
ipn=re.findall(r'r/>(.*?)<b',html.text,re.S)
for ip in ipn:
    i=re.sub('\n','',ip)
    iplist.append(i.strip())
    print(i.strip())
print(iplist)