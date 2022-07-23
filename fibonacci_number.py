# Author: leetcode + kei
# Date: July 23, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest

# I think these three solutions below are good enough for interview.


class Solution:
    '''
    Recursion
    O(N^2) time, O(N) space
    '''

    def __init__(self):
        pass

    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)


class Solution2:
    '''
    Top down DP
    O(N) time and space
    '''

    def __init__(self):
        self.memo = dict()
        pass

    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            self.memo[n] = n
            return self.memo[n]

        if n in self.memo:
            return self.memo[n]

        self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.memo[n]


class Solution3:
    '''
    Bottom up DP
    O(N) time, O(1) space
    '''

    def __init__(self):
        pass

    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        prev2 = 0
        prev1 = 1
        for i in range(n - 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return curr


class TestSolution(unittest.TestCase):

    # def test_solve(self):
    #     '''
    #     Test
    #     '''
    #     input_and_expected_outputs = [
    #         # (input1, input2, expected output) depending on number of arguments
    #         ([0, 1, 2], 3, 6),
    #         ([0, 1], 3, 5),
    #     ]
    #     s = Solution()
    #     for input1, input2, expected in input_and_expected_outputs:
    #         with self.subTest(input1=input1, input2=input2, expected=expected):
    #             result = s.solve(input1, input2)
    #             self.assertEqual(result, expected)

    def test_tree(self):
        '''
        Tree test example
        '''
        # Binary Tree
        #     6
        #    /  \
        #   3    12
        #  / \   / \
        # 1   4 9  14

        n1 = TreeNode(6)
        n2 = TreeNode(3)
        n3 = TreeNode(12)
        n4 = TreeNode(1)
        n5 = TreeNode(4)
        n6 = TreeNode(9)
        n7 = TreeNode(14)

        n1.left = n2
        n1.right = n3
        n2.left = n4
        n2.right = n5
        n3.left = n6
        n3.right = n7

        s = Solution()
        input_and_expected_outputs = [
            # (input1, input2, expected output) depending on number of arguments
            (n1, n6, n7, n3),
            (n1, n3, n5, n1),
            (n1, n4, n5, n1),  # Fail
        ]
        s = Solution()
        for input1, input2, input3, expected in input_and_expected_outputs:
            with self.subTest(input1=input1.val, input2=input2.val, input3=input3.val,
                              expected=expected.val):
                result = s.solve(input1, input2, input3)
                self.assertEqual(result, expected)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
