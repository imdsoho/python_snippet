
def type_func():
    begin = 1
    step = 2
    result = type(begin + step)(begin)
    # print(type(begin + step))   # <class 'int'>
    # print(int(1))
    print(result)


if __name__ == '__main__':
    type_func()
