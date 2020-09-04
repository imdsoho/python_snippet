import time
import random

from concurrent.futures import ThreadPoolExecutor


def some_task(n):
    time.sleep(n)
    print("Task {} finished".format(n))
    return n


def process():
    result_data = {}
    with ThreadPoolExecutor(max_workers=4) as executor:
        try:
            task1 = executor.submit(some_task, (1))
            result_data['t1'] = task1
            task2 = executor.submit(some_task, (2))
            result_data['t2'] = task2
            executor.shutdown(wait=True)
            task3 = executor.submit(some_task, (3))
            result_data['t3'] = task3
            task4 = executor.submit(some_task, (4))
            result_data['t4'] = task4
        except Exception as e:
            print("Exception - {}".format(e))
            result_data['error'] = 'exception'

    return result_data


def main():
    data = process()
    print(data)


if __name__ == "__main__":
    main()
