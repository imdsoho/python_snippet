import threading
import time


class myWorker():

    def __init__(self):
        self.a = 1
        self.b = 2
        self.rlock = threading.Lock()
        print("__init__ {}".format(self.rlock))

    def modifyA(self):
        with self.rlock:
            print("Modifying A : RLock Acquired: {}".format(self.rlock._is_owned()))
            print("[A] {}".format(self.rlock))
            self.a = self.a + 1
            time.sleep(1)

    def modifyB(self):
        with self.rlock:
            print("Modifying B : RLock Acquired: {}".format(self.rlock._is_owned()))
            print("[B] {}".format(self.rlock))
            self.b = self.b - 1
            time.sleep(1)

    def modifyBoth(self):
        with self.rlock:
            print("Rlock acquired, modifying A and B")
            print("[2-1] {}".format(self.rlock))
            self.modifyA()
            print("[2-2] {}".format(self.rlock))
            self.modifyB()
        print("[2-3] {}".format(self.rlock))


workerA = myWorker()
workerA.modifyBoth()
