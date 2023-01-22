import queue


class IteratorPipe:

    def __init__(self, sentinel=None):
        self._q = queue.Queue()
        self._sentinel = sentinel

    def __iter__(self):
        return self

    def __next__(self):
        data = self._q.get(block=True)
        if data is self._sentinel:
            raise StopIteration

        return data

    def put(self, data):
        self._q.put(data)