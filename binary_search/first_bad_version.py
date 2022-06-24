# Author: leetcode + kei
# Date: May 15, 2022
import unittest
from typing import *
from helper_classes import *
import numpy as np


class Solution:
    def __init__(self):
        pass

    # The isBadVersion API is already defined for you.
    def isBadVersion(self, version: int) -> bool:
        pass

    def firstBadVersion(self, n: int) -> int:
        '''
        Binary Search to find leftmost x
        '''
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            ret = self.isBadVersion(mid)
            if ret:
                right = mid - 1
            else:
                left = mid + 1
        return left


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
