import random,time,queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

task_queue=queue.Queue()
result_queue=queue.Queue()

class QueueManger(BaseManager):
    pass

def return_task_queue():
    global task_queue
    return task_queue
def return_result_queue():
    global result_queue
    return result_queue

def test():
    QueueManger.register('get_task_queue', callable=return_task_queue)
    QueueManger.register('get_result_queue', callable=return_result_queue)

    manger = QueueManger(address=('127.0.0.1', 5000), authkey=b'abc')
    manger.start()

    task = manger.get_task_queue()
    result = manger.get_result_queue()

    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d' % n)
        task.put(n)

    print('Try to get results...')

    for i in range(n):
        r = result.get(timeout=15)
        print('Result:%s' % r)

    manger.shutdown()
    print('master exit')

if __name__=='__main__':
    freeze_support()
    test()