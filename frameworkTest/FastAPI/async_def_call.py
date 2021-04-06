import time
from fastapi import APIRouter, Query

import asyncio
import aiohttp

# API namespace
router = APIRouter()


async def call_web_site(url):
    # 4.494582653045654
    '''resp = requests.get(url)
    response = resp.status_code'''

    # 0.8705756664276123
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            response = await resp.text()

    return response


@router.get("/asynctest", summary="async get test", description="api 여러개를 async로 실행하는 것을 테스트하는 api")
async def get_async_test():
    s1 = time.time()

    func_list = [
        call_web_site("https://httpbin.org/anything"),
        call_web_site("https://httpbin.org/anything"),
        call_web_site("https://httpbin.org/anything"),
        call_web_site("https://httpbin.org/anything"),
        call_web_site("https://httpbin.org/anything")
    ]
    result = await asyncio.gather(*func_list) # 모든 비동기 함수를 동시에 선언한다.

    print(time.time() - s1)
    return result
