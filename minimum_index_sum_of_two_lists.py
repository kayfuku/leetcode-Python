# Author: leetcode + kei
# Date: May 25, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest


class Solution:
    def __init__(self):
        pass

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        # Search common thing => use dict.
        map = {}
        for i, s in enumerate(list1):
            map[s] = i

        min = float('inf')
        sum = 0
        for j, t in enumerate(list2):
            if t not in map:
                continue

            sum = j + map[t]
            if sum < min:
                res.clear()
                res.append(t)
                min = sum
            elif sum == min:
                res.append(t)

        return res


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
