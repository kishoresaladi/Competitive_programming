import unittest


def change_possibilities(amt, p):

    
    change = [0] * (amt + 1)
    change[0] = 1
    for i in p:
        for x in range(i, amt + 1):
            rem = x - i
            change[x] += (change[rem])
    return change[amt]
    

    


















# Tests

class Test(unittest.TestCase):

    def test_sample_input(self):
        actual = change_possibilities(4, (1, 2, 3))
        expected = 4
        self.assertEqual(actual, expected)

    def test_one_way_to_make_zero_cents(self):
        actual = change_possibilities(0, (1, 2))
        expected = 1
        self.assertEqual(actual, expected)

    def test_no_ways_if_no_coins(self):
        actual = change_possibilities(1, ())
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_coin_value(self):
        actual = change_possibilities(5, (25, 50))
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_target_amount(self):
        actual = change_possibilities(50, (5, 10))
        expected = 6
        self.assertEqual(actual, expected)

    def test_change_for_one_dollar(self):
        actual = change_possibilities(100, (1, 5, 10, 25, 50))
        expected = 292
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)