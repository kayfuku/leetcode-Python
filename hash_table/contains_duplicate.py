# Author: leetcode + kei
# Date: May 22, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest


class Solution:
    def __init__(self):
        pass

    def containsDuplicate(self, nums: List[int]) -> bool:
        _set = set()
        for num in nums:
            if num in _set:
                return True
            _set.add(num)

        return False


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        For more than one argument
        For one argument, comment out some lines.
        '''
        input_and_expected_outputs = [
            # ((input), expected output) or
            # (input, expected output) depending on number of arguments
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
