import functools
import asyncio
import threading
# def consumer():
# 	r=''
# 	while True:
# 		n=yield r
# 		if not n:
# 			return
# 		print('[CONSUMER] Consuming %s...' % n)
# 		r='200 OK'

# def produce(c):
# 	c.send(None)
# 	n=0
# 	while n<5:
# 		n=n+1
# 		print('[PRODUCER] Producing %s...' % n)
# 		r=c.send(n)
# 		print('[PRODUCER] Consumer return: %s' % r)
# 	c.close()

# c=consumer()
# produce(c)

#装饰器的用法
# def log(func):
# 	print("AAA")
# 	# @functools.wraps(func)
# 	def wrapper(*args, **kw):
# 		print('call %s():' % func.__name__)
# 		return func(*args, **kw)
# 	return wrapper
# 	print("BBB")

# @log
# def now():
# 	print("+-+-+-+-")

# now()
# print(now.__name__)

#asyncio的用法
# async def hello():
# 	print(r"你好。\(@^0^@)/   (%s)" % threading.currentThread())
# 	r=await asyncio.sleep(1)
# 	print(r"ヽ(￣ω￣(￣ω￣〃)ゝ哈皮   (%s)" % threading.currentThread())

# loop=asyncio.get_event_loop()
# tasks=[hello(),hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

#asyncio的实例
async def wget(host):
	print('wget %s...' % host)
	connect=asyncio.open_connection(host,80)
	reader,writer=await connect
	header='GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
	writer.write(header.encode('utf-8'))
	await writer.drain()
	while True:
		line=await reader.readline()
		if line == b'\r\n':
			break
		print('%s header > %s' %(host,line.decode('utf-8').rstrip()))
	writer.close()

loop=asyncio.get_event_loop()
tasks=[wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()