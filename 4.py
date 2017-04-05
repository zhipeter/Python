import os
from multiprocessing import Process
import subprocess
import time,threading

def run(name):
    print('Run child Proess %s (%s) start' % (name,os.getpid()))

# if __name__=='__main__':
#     print('Parent Process %s' % os.getpid())
#     p=Process(target=run,args=('test',))
#     print('Child Process will start.')
#     p.start()
#     p.join()
#     print('Child Process end')

# r=subprocess.call(['nslookup','www.tongji.edu.cn'])
# print('Exit code:', r)

# def loop():
#     print('thread %s is running' % threading.current_thread().name)
#     n=0
#     while n<5:
#         n+=1
#         print('thread %s >>> %s' % (threading.current_thread().name,n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)

# print('thread %s is running' % threading.current_thread().name)
# t=threading.Thread(target=loop,name='Zhi')
# t.start()
# t.join()
# print('thread %s is running' % threading.current_thread().name)


# balance=0
# lock=threading.Lock()

# def chang_it(n):
# 	global balance
# 	balance+=n
# 	balance-=n

# def run_thread(n):
# 	for i in range(100000):
# 		lock.acquire()
# 		try:
# 			chang_it(n)
# 		finally:
# 			lock.release()

# def run_thread2(n):
# 	for i in range(100000):
# 		chang_it(n)

# t1=threading.Thread(target=run_thread, args=(5,))
# t2=threading.Thread(target=run_thread, args=(8,))
# print('Start: %s' % time.ctime())
# start1=time.time()
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)
# end1=time.time()
# print('End: %s, time is %0.002f' % (time.ctime(),end1-start1))

# td=threading.Thread(target=run_thread2,args=(6,))
# print('Start: %s' % time.ctime())
# start1=time.time()
# td.start()
# td.join()
# print(balance)
# end1=time.time()
# print('End: %s, time is %0.002f' % (time.ctime(),end1-start1))
# print('Start: %s' % time.ctime())
# time.sleep(5)
# print('Start: %s' % time.ctime())


# local_1=threading.local()
# def process_student():
# 	std=local_1.name
# 	print('Hello, %s (in %s)' % (std, threading.current_thread().name))

# def process_thread(name):
# 	local_1.name=name
# 	process_student()

# process_thread('Wang')

# x='Python'

# def find_indir(path):
# 	if os.path.isdir(path):
# 		if x in os.path.split(path)[1]:
# 			print(path)
# 			for i in os.listdir(path):
# 				find_indir(os.path.join(path,i))
# 		else:
# 			for i in os.listdir(path):
# 				find_indir(os.path.join(path,i))
# 	else:
# 		if x in os.path.splitext(path)[0].split('\\')[-1]:
# 			print(path)

# find_indir('C:\\Users\\ZHI\\Documents\\GitHub')

# import json

# class Student(object):
#     """docstring for Student"""
#     def __init__(self, name,age,score):
#         self.name=name
#         self.age=age
#         self.score = score

# s=Student('VVV',22,34)
# print(json.dumps(s,default=lambda obj:obj.__dict__))
def foo(s):
    '''
	Function to get absolute:
	Example:

	>>>abs(1)
	1
	>>>abs(-1)
	1
    '''
    n = int(s)
    assert n!=0, 'n is 0'
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
