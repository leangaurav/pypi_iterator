![Build](https://github.com/leangaurav/pypi_iterator/actions/workflows/python-package.yml/badge.svg?branch=main&event=push)

Available at [PyPi](https://pypi.org/project/iterators/)

Provides a wrapper class TimeoutIterator to add timeout feature to normal iterators

### Installation:

    pip install iterators


See help of TimeoutIterator for all the features. Check tests for examples on how to use TimeoutIterator.
See example tests below for basic  usage

### Example:

1. TimeoutIterator works like normal iterator:

    ```
    from iterators import TimeoutIterator

    def iter_simple():
        yield 1
        yield 2

    def test_normal_iteration(self):
        i = iter_simple()
        it = TimeoutIterator(i)

        self.assertEqual(next(it), 1)
        self.assertEqual(next(it), 2)

        self.assertRaises(StopIteration, next, it)
        self.assertRaises(StopIteration, next, it)
    ```

1. When timeout is needed, use like this
    ```    
    def iter_with_sleep():
        yield 1
        time.sleep(0.6)
        yield 2
        time.sleep(0.4)
        yield 3

    def test_fixed_timeout(self):
        i = iter_with_sleep()
        it = TimeoutIterator(i, timeout=0.5)
        self.assertEqual(next(it), 1)
        self.assertEqual(next(it), it.get_sentinel())
        
        self.assertEqual(next(it), 2)
        self.assertEqual(next(it), 3)
        self.assertRaises(StopIteration, next, it)
    ```

1. Dynamic timeout adjustment
    ```
    def iter_with_sleep():
        yield 1
        time.sleep(0.6)
        yield 2
        time.sleep(0.4)
        yield 3

    def test_timeout_update(self):
        i = iter_with_sleep()
        it = TimeoutIterator(i, timeout=0.5)
        self.assertEqual(next(it), 1)
        self.assertEqual(next(it), it.get_sentinel())
        
        it.set_timeout(0.3)
        self.assertEqual(next(it), 2)
        self.assertEqual(next(it), it.get_sentinel())

        self.assertEqual(next(it), 3)
        self.assertRaises(StopIteration, next, it)
    ```

### Run unit tests locally:
    python -m unittest discover tests
