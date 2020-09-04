import time
import random
import functools

from concurrent.futures import ThreadPoolExecutor


def some_task(n):
    time.sleep(3)
    print("Task {} finished".format(n))
    return n


def f_callback(future):
    print("Future: {} - Status: {}, Error: {}".format(future, future.done(), future.exception()))


def process():
    result_data = {}
    with ThreadPoolExecutor(max_workers=1) as executor:
        try:
            future1 = executor.submit(some_task, (1))
            future2 = executor.submit(some_task, (2))
            future1.add_done_callback(functools.partial(print, "Future:"))
            # future1.add_done_callback(f_callback)
            # print("[notify] ", future1.set_running_or_notify_cancel())
            # print("[notify]", future2.set_running_or_notify_cancel())

            # print(future1.running())
            print(future2.cancel())

            # print(future1.exception(timeout=None))
            print("[1]", future1.result())
            print("[2]", future2.result())

            result_data['t1'] = future1.result()
            result_data['t2'] = future2.result()
        except Exception as e:
            print("Exception - {}".format(e))

    return result_data


def main():
    data = process()
    print(data)


if __name__ == "__main__":
    main()
