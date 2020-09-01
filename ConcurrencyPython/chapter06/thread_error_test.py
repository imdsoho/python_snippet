import sys
import threading
import time
import queue


def myThread(queue):
    while True:
        try:
            time.sleep(1)

            raise Exception('Exception Thrown In Child Thread {}'.format(threading.current_thread()))
        except:
            queue.put(sys.exc_info())


queue = queue.Queue()
myThread = threading.Thread(target=myThread, args=(queue,))
myThread.start()

while True:
    try:
        exception = queue.get()
    except queue.Queue.Empty:
        pass
    else:
        print(exception)
        break
