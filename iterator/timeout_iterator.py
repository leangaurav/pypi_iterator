import queue
import threading

class TimeoutIterator:
    """
    Wrapper class to add timeout feature to synchronous iterators
    - timeout: initial default timeout
    - sentinel: the object returned by iterator when timeout happens
    - timeout_reset: if set to True, timeout is reset to the value of ZERO_TIMEOUT on each iteration 

    TimeoutIterator uses a thread internally. 
    The thread stops once the iterator exhausts or raises an exception during iteration.

    Any excptions raised within the wrapped iterator are popagated as it is.
    The excption is raised only on reaching the element after which raised by actual iterator
    Timeout can be set dynamically before going for iteration
    """
    ZERO_TIMEOUT = 0.0

    def __init__(self, iterator, timeout=0.0, sentinel=object(), timeout_reset=False):
        self._iterator = iterator
        self._timeout = timeout
        self._sentinel= sentinel
        self._timeout_reset = timeout_reset
        
        self._done = False
        self._buffer = queue.Queue()
        self._thread = threading.Thread(target=self.__lookahead)
        self._thread.start()
        
    def get_sentinel(self):
        return self._sentinel
        
    def set_timeout_reset(self, timeout_reset):
        self._timeout_reset = reset

    def set_timeout(self, timeout: float):
        """
        Set timeout for next iteration
        """
        self._timeout = timeout

    def __iter__(self):
        return self

    def __next__(self):
        """
        yield the result from iterator
        if timeout > 0:
            yield data if available.
            otherwise yield sentinal
        """
        if self._done:
            raise StopIteration

        data = self._sentinel
        try:
            if self._timeout > self.ZERO_TIMEOUT:
                data = self._buffer.get(timeout=self._timeout)
            else:
                data = self._buffer.get()
        except queue.Empty:
            pass
        finally:
            # see if tiemout needs to be reset
            if self._timeout_reset:
                self._timeout = self.ZERO_TIMEOUT

        # propagate any exceptions including StopIteration
        if isinstance(data, BaseException):
            self._done = True
            raise data

        return data

    def __lookahead(self):
        try:
            while True:
                self._buffer.put(next(self._iterator))
        except BaseException as e:
            self._buffer.put(e)
