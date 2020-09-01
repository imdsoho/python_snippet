from threading import Lock
from functools import wraps


def locked_method(method):
    @wraps(method)
    def newmethod(self, *args, **kwargs):
        with self._lock:
            return method(self, *args, **kwargs)
    return newmethod


class DecoratorLockedSet(set):
    def __init__(self, *args, **kwargs):
        self._lock = Lock()
        super().__init__(*args, **kwargs)

    @locked_method
    def add(self, elem):
        return super().add(elem)

    @locked_method
    def remove(self, elem):
        return super().remove(elem)


dlset = DecoratorLockedSet()
dlset.add('hello')
print(dlset)

libset = set()
libset.add('python')
print(libset)