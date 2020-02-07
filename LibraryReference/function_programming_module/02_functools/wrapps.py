from functools import wraps
def my_decorator(f):
    #@wraps(f)      # 1: wrapper
                    # 2: None
    @wraps(f)       # 1: example
                    # 2: Docstring
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)

    return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')

example()

print("1: ", example.__name__)
print("2: ", example.__doc__)

print(example.__dict__)         # {'__wrapped__': <function example at 0x00294>}
print(example.__wrapped__())    # Called example function
