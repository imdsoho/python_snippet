from threading import Lock


class LockedSet(set):
    def __init__(self, *args, **kwargs):
        self._lock = Lock()
        super().__init__(*args, **kwargs)
        # super(LockedSet, self).__init__(*args, **kwargs)  # python 2.x

    def add(self, elem):
        with self._lock:
            super().add(elem)

    def remove(self, elem):
        with self._lock:
            super().remove(elem)

    def __contains__(self, elem):
        with self._lock:
            super().__contains__(elem)
