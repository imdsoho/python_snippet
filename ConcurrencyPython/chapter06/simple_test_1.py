import unittest


def simple_function(x):
    return x + 1


class SimpleFunctionTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_simple_function(self):
        pass


if __name__ == '__main__':
    unittest.main()
