import unittest


def sort_algorithm(A: list):
    pass


def is_not_in_descending_order(a):
    """
    Check if the list a is not descending (means "rather ascending")
    """
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False
    return True


class TestSort(unittest.TestCase):
    def test_simple_cases(self):
        cases = ([1], [], [1, 2], [1, 2, 3, 4, 5],
                 [4, 2, 5, 1, 3], [5, 4, 4, 5, 5],
                 list(range(10)), list(range(10, 0, -1)))
        for b in cases:
            with self.subTest(i=b):
                a = list(b)
                sort_algorithm(a)
                self.assertCountEqual(a, b)
                self.assertTrue(is_not_in_descending_order(a))


if __name__ == "__main__":
    unittest.main()