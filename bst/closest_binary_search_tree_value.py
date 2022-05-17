# Author: leetcode + kei
# Date: May ?, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest


class Solution:
    def __init__(self):
        pass

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        node = root
        while node:
            val = node.val
            closest = val if abs(
                val - target) < abs(closest - target) else closest
            if val > target:
                node = node.left
            else:
                node = node.right

        return closest


class TestCalc(unittest.TestCase):

    # def test_solve1(self):
    #     '''
    #     For one argument
    #     '''
    #     input_and_expected_outputs = [
    #         # (input, expected output)
    #         (1, 1),
    #         (2, 1),
    #         (4, 2),
    #         (8, 2),
    #         (10, 3),
    #     ]
    #     s = Solution()
    #     for input, expected in input_and_expected_outputs:
    #         result = s.solve(input)
    #         self.assertEqual(result, expected)

    def test_solve2(self):
        '''
        For more than one argument
        '''
        input_and_expected_outputs = [
            # ((input), expected output)
            (([0, 1, 2], 3), 6),
            (([0, 1], 3), 5),
        ]
        s = Solution()
        for input, expected in input_and_expected_outputs:
            result = s.solve(*input)
            self.assertEqual(result, expected)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
