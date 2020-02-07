from functools import partial

def sum(a, b):
    print(a/b)

f = partial(sum, 10)
print(type(f))
print(f(2))
