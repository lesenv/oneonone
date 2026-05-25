import unittest as ut
import add_for_test as mult

class TestAddFunction(ut.TestCase):

    def test_add_postive_numbers(self):
        self.test_cases = [
            {"a": 1, "b": 2, "expected": 3},
            {"a": 1, "b": "strin", "expected": 'b has to be a number'},
            {"a": [1, 2, 8], "b": 2, "expected": "a has to be a number"},
            {"a": -2, "b": 2, "expected": 0},
            {"a": 1.8, "b": 2.2, "expected": 4.0},
            ]
        self.assertEqual(mult.add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(mult.add(-2, -3), -5)

    def test_add_string(self):
        self.assertEqual(mult.add(1, "string"), 'b has to be a number')

    def test_add_string(self):
        with self.assertRaises(TypeError) as cm:
            mult.add(3, "nuiiad")
        self.assertEqual('b has to be a number', str(cm.exception))

    def test_add_list(self):
        with self.assertRaises(TypeError) as cm:
            mult.add([1,2,0], 4)
        self.assertEqual("a has to be a number", str(cm.exception))

    def test_add_floats(self):
        self.assertEqual(mult.add(1.2, 4.8), 6.0)

if __name__ == "__main__":
    ut.main()