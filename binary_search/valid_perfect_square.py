# Author: leetcode + kei
# Date: May 18, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest


class Solution:
    def __init__(self):
        pass

    def isPerfectSquare(self, num: int) -> bool:
        # Find square root using Binary Search
        left = 1
        right = num
        while left <= right:
            # You don't have to worry about overflow in Python.
            mid = (left + right) // 2
            squared = mid * mid
            if squared == num:
                return mid
            if squared > num:
                right = mid - 1
            else:
                left = mid + 1

        return False


class TestCalc(unittest.TestCase):

    def test_solve(self):
        '''
        For more than one argument
        For one argument, comment out some lines.
        '''
        input_and_expected_outputs = [
            # ((input), expected output) or
            # (input, expected output)
            (([0, 1, 2], 3), 6),
            (([0, 1], 3), 5),
        ]
        s = Solution()
        for input, expected in input_and_expected_outputs:
            # result = s.solve(input)
            result = s.solve(*input)
            self.assertEqual(result, expected)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
