# Author: leetcode + kei
# Date: May 14, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest


class Solution:
    def __init__(self):
        pass

    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        # Binary Search
        # sqrt should be in between 1 and x.
        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2
            squared = self.mono(mid)
            if squared == x:
                return mid
            if squared > x:
                right = mid - 1
            else:
                left = mid + 1
        # Why is this? Test it for all possible cases.
        return right  # OK
        # return left  # failed
        # return right + 1  # failed

    def mono(self, a):
        # This must be monotonically increasing/decreasing function.
        return a * a


class TestCalc(unittest.TestCase):

    def test_mySqrt(self):
        input_and_expected_outputs = [
            # ((input), expected output)
            (1, 1),
            (2, 1),
            (4, 2),
            (8, 2),
            (10, 3),
        ]
        s = Solution()
        for input, expected in input_and_expected_outputs:
            result = s.mySqrt(input)
            self.assertEqual(result, expected)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
