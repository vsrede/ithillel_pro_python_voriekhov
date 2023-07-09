
from decimal import Decimal


class frange:
    """
    Сlass equivalent to the range() function, but only works with int and float (range() is not working with float)
    """
    def __init__(self, *args):
        if len(args) > 3 or len(args) == 0:
            raise TypeError("Range expected 1 to 3 arguments")
        elif len(args) == 3:
            self._start = args[0]
            self._limit = args[1]
            self._step = args[2]
        elif len(args) == 2:
            self._start = args[0]
            self._limit = args[1]
            self._step = 1
        else:
            self._start = 0
            self._limit = args[0]
            self._step = 1

    def __next__(self):
        self._step = Decimal(self._step)
        if self._step > 0 and self._start >= self._limit:
            raise StopIteration("END")
        elif self._step < 0 and self._start <= self._limit:
            raise StopIteration("END")

        result = Decimal(self._start)
        self._start = Decimal(self._start) + Decimal(self._step)
        return result

    def __iter__(self):
        return self


# assert(list(frange(5)) == [0, 1, 2, 3, 4])
# assert(list(frange(2, 5)) == [2, 3, 4])
# assert(list(frange(2, 10, 2)) == [2, 4, 6, 8])
# assert(list(frange(10, 2, -2)) == [10, 8, 6, 4])
# assert(list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
# assert(list(frange(1, 5)) == [1, 2, 3, 4])
# assert(list(frange(0, 5)) == [0, 1, 2, 3, 4])
# assert(list(frange(0, 0)) == [])
# assert(list(frange(100, 0)) == [])
# assert (list(frange(1, 2, 3, 4, 5, )))