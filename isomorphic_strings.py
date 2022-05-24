# Author: leetcode + kei
# Date: May 24, 2022
import re
from typing import *
from helper_classes import *
import numpy as np
import unittest


class Solution:
    def __init__(self):
        pass

    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_idx = {}
        map_t_idx = {}
        for i, (c1, c2) in enumerate(zip(s, t)):
            # Use get(key, default) instead of map[key] or
            # use defaultdict from collections.
            if map_s_idx.get(c1, -1) != map_t_idx.get(c2, -1):
                return False
            map_s_idx[c1] = i
            map_t_idx[c2] = i

        return True


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
