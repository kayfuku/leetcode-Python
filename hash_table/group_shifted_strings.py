# Author: leetcode + kei
# Date: May 28, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest


class Solution:
    def __init__(self):
        pass

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = {}
        for s in strings:
            key = ()
            for i in range(1, len(s)):
                diff = ord(s[i]) - ord(s[i - 1])
                # Just memorize to add 26.
                circular_diff = (diff + 26) % 26
                key += (circular_diff, )
            # Add the string to the list and put the list to the dict.
            groups[key] = groups.get(key, []) + [s]

        return list(groups.values())


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
