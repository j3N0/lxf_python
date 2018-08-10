#-*-coding:utf-8-*-

import random, time, queue
from multiprocessing.managers import BaseManager
from multiprocessing import Process

task_queue = queue.Queue()
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

def master_process():
    QueueManager.register('get_task_queue', callable=lambda:task_queue)
    QueueManager.register('get_result_queue', callable=lambda:result_queue)

    manager = QueueManager(address = ('', 5000), authkey = b'abc')
    manager.start()
    
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0, 1000)
        print('Put task %d..' % n)
        task.put(n)

    print('Try get result...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)
    manager.shutdown()
    print('master exit.')

def worker_process():
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    server_addr = '127.0.0.1'
    print('Connect to server %s...' % server_addr)
 
    time.sleep(5)
    m = QueueManager(address=(server_addr, 5000), authkey = b'abc')
    m.connect()

    task = m.get_task_queue()
    result = m.get_result_queue()

    for i in range(10):
        try:
            n = task.get(timeout=1)
            print('run task %d * %d....', (n, n))
            r = '%d * %d = %d' % (n, n, n * n)
            time.sleep(1)
            result.put(r)
        except Queue.Empty:
            print('task queue is empty.')
    print('worker exit')

if __name__ == '__main__':
    master = Process(target=master_process)
    worker = Process(target=worker_process)
    master.start()
    worker.start()
    
    worker.join()
    master.join()
    print('END')
