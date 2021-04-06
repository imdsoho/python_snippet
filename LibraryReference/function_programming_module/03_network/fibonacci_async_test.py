from time import time, sleep
import random

import asyncio


async def fibonach(member_id, num):
    await asyncio.sleep(0.5)
    for i in range(0, 10):
        answer = 0
        f0 = 0
        f1 = 1
        if num < 2:
            return num
        else:
            for i in range(1, num):
                answer = f1 + f0
                f0 = f1
                f1 = answer

    return member_id, i, answer


async def fetch(member_id):
    if member_id == 0: num = 500
    elif member_id == 1: num = 400
    elif member_id == 2: num = 300
    elif member_id == 3: num = 200
    else: num = 100

    response = await fibonach(member_id, num)
    return response


async def main():
    futures = [asyncio.ensure_future(fetch(member_id)) for member_id in range(0, 5)]
    result = await asyncio.gather(*futures)
    print(result)


def sync_fibonach(member_id, num):
    sleep(0.5)
    for i in range(0, 10):
        answer = 0
        f0 = 0
        f1 = 1
        if num < 2:
            return num
        else:
            for i in range(1, num):
                answer = f1 + f0
                f0 = f1
                f1 = answer

    return member_id, i, answer


def sync_fetch(member_id):
    if member_id == 0: num = 500
    elif member_id == 1: num = 400
    elif member_id == 2: num = 300
    elif member_id == 3: num = 200
    else: num = 100

    response = sync_fibonach(member_id, num)
    return response


def sync_main():
    result = []

    for member_id in range(0, 5):
        response = sync_fetch(member_id)
        result.append(response)

    print(result)


begin = time()

# 실행 시간: 0.507초
loop = asyncio.get_event_loop()     # 이벤트 루프를 얻음
loop.run_until_complete(main())     # main이 끝날 때까지 기다림
loop.close()                        # 이벤트 루프를 닫음

# 실행 시간: 2.506초
# sync_main()

end = time()
print('실행 시간: {0:.3f}초'.format(end - begin))