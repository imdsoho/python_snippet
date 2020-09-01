import threading
import queue
import time


def mySubscriber(queue):
    time.sleep(1)

    while not queue.empty():
        item = queue.get()

        if item is None:
            break

        print("{} removed {} from the queue".format(threading.current_thread(), item))
        queue.task_done()


myQueue = queue.Queue()
for i in range(5):
    myQueue.put(i)

print("Queue Populated")


if __name__ == "__main__":
    thread1 = threading.Thread(target=mySubscriber, args=(myQueue,))
    thread1.start()
    thread2 = threading.Thread(target=mySubscriber, args=(myQueue,))
    thread2.start()

    print("Not Progressing Till Queue is Empty")
    myQueue.join()
    print("Queue is now empty")
    thread1.join()
    thread2.join()

    print("Main thread End")