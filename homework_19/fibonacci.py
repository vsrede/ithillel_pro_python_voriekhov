import unittest


class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]


class TestFibonacci(unittest.TestCase):

    def setUp(self):
        self.fib = Fibonacci()

    def test_valid(self):
        self.assertEqual(self.fib(6), 8)

    def test_zero(self):
        self.assertEqual(self.fib(0), 0)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            self.fib(-1)

    def test_str(self):
        with self.assertRaises(ValueError):
            self.fib("0")

    def test_float(self):
        with self.assertRaises(ValueError):
            self.fib(3.14)

    def test_more_arguments(self):
        with self.assertRaises(TypeError):
            self.fib(1, 2)

    def test_large(self):
        self.assertEqual(self.fib(400),
                         176023680645013966468226945392411250770384383304492191886725992896575345044216019675)


if __name__ == '__main__':
    unittest.main()