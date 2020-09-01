import timeit
import time


def func1():
    print("Function 1 - start")
    time.sleep(3)
    print("Function 1 - stop")


def func2():
    print("Function 2 - start")
    time.sleep(4)
    print("Function 2 - stop")


'''start_time = timeit.default_timer()
func1()
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
func2()
print(timeit.default_timer() - start_time)'''


t1 = timeit.Timer("func1()", setup="from __main__ import func1")
times = t1.repeat(repeat=2, number=1)
for t in times:
    print("{} seconds: ".format(t))

