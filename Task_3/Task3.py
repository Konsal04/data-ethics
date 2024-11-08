def cyclic_time_difference(hour1, hour2):

    direct_diff = abs(hour1 - hour2)
    cyclic_diff = 24 - direct_diff
    return min(direct_diff, cyclic_diff)


import unittest


class TestCyclicTimeDifference(unittest.TestCase):
    def test_same_hour(self):
        self.assertEqual(cyclic_time_difference(0, 0), 0)
        self.assertEqual(cyclic_time_difference(12, 12), 0)

    def test_one_hour_difference(self):
        self.assertEqual(cyclic_time_difference(1, 2), 1)
        self.assertEqual(cyclic_time_difference(23, 0), 1)

    def test_opposite_hours(self):
        self.assertEqual(cyclic_time_difference(0, 12), 12)
        self.assertEqual(cyclic_time_difference(12, 0), 12)

    def test_cross_midnight(self):
        self.assertEqual(cyclic_time_difference(23, 1), 2)
        self.assertEqual(cyclic_time_difference(22, 2), 4)

    def test_arbitrary_hours(self):
        self.assertEqual(cyclic_time_difference(3, 15), 12)
        self.assertEqual(cyclic_time_difference(6, 18), 12)
        self.assertEqual(cyclic_time_difference(8, 23), 9)


if __name__ == "__main__":
    unittest.main()
