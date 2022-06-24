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


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_outputs = [
            # (input1, input2, expected output) depending on number of arguments
            ([0, 1, 2], 3, 6),
            ([0, 1], 3, 5),
        ]
        s = Solution()
        for input1, input2, expected in input_and_expected_outputs:
            with self.subTest(input1=input1, input2=input2, expected=expected):
                result = s.solve(input1, input2)
                self.assertEqual(result, expected)

    # def test_tree(self):
    #     '''
    #     Tree test example
    #     '''
    #     n1 = TreeNode(5)
    #     n2 = TreeNode(1)
    #     n3 = TreeNode(5)
    #     n4 = TreeNode(5)
    #     n5 = TreeNode(5)
    #     n6 = TreeNode(5)

    #     n1.left = n2
    #     n1.right = n3
    #     n3.right = n6
    #     n2.left = n4
    #     n2.right = n5

    #     s = Solution()
    #     result = s.countUnivalSubtrees(n1)
    #     self.assertEqual(result, 4)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
