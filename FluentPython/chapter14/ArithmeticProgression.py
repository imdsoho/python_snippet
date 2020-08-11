class ArithmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    # 반복형(iterable)은 __iter__()를 구현하되, __next__()는 구현하면 안된다.
    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index+=1
            result = self.begin + self.step * index


if __name__ == '__main__':
    ap = ArithmeticProgression(0, 1, 3)
    print(type(ap))
    print(list(ap))

