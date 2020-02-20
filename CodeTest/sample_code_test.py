# https://python.flowdas.com/library/collections.html#counter-objects
# Counter 예제 코드
from collections import Counter
from itertools import combinations_with_replacement

data = map(Counter, combinations_with_replacement('ABC', 2))
for value in data:
    #print(value)
    pass


# https://python.flowdas.com/library/collections.html#deque-objects
# roundrobin() 예제 코드
from collections import deque

def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"

    #iterators = deque(map(iter, *iterables))
    iterators = deque(map(iter, iterables))
    # type(iterators) - deque
    # iterators value
    #['A', 'B', 'C']
    #['D']
    #['E', 'F']

    while iterators:
        try:
            while True:
                # 한 문자씩 next()로 사용
                yield next(iterators[0])

                # 데크를 n 단계 오른쪽으로 회전합니다. n이 음수이면, 왼쪽으로 회전합니다.
                iterators.rotate(-1)

        except StopIteration:
            # 소진된 이터레이터를 제거합니다.
            iterators.popleft()

#for it in roundrobin(['ABC', 'D', 'EF']):
for it in roundrobin('ABC', 'D', 'EF'):
    print(it)
    #pass
