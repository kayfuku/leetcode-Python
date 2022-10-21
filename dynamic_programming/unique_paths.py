# Author: leetcode + kei
# Date: October 21, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    DP
    O(mn) time and space
    '''

    def uniquePaths(self, m: int, n: int) -> int:
        d = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                # num of ways from above and left
                d[row][col] = d[row - 1][col] + d[row][col - 1]

        return d[m - 1][n - 1]


class Solution2:
    '''
    DP
    O(mn) time and space
    '''

    def uniquePaths(self, m: int, n: int) -> int:
        d = [[0] * n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    d[row][col] = 1
                else:
                    # num of ways from above and left
                    d[row][col] = d[row - 1][col] + d[row][col - 1]

        return d[m - 1][n - 1]


class Solution3:
    '''
    DP
    O(mn) time, O(n) space
    '''

    def uniquePaths(self, m: int, n: int) -> int:
        cur_r = [1] * n
        for r in range(1, m):
            for c in range(1, n):
                cur_r[c] += cur_r[c - 1]

        return cur_r[-1]


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_output = [
            # (input1, input2, expected output) depending on number of arguments
            ([0, 1, 2], 3, 6),
            ([0, 1], 3, 5),
        ]
        s = Solution()
        for case, (input1, input2, expected) in enumerate(
                input_and_expected_output):
            print('Case: {}'.format(case))
            with self.subTest(input1=input1, input2=input2, expected=expected):
                result = s.topKFrequent(input1, input2)
                self.assertEqual(result, expected)

    # def test_tree(self):
    #     '''
    #     Tree test example
    #     '''
    #     # Binary Tree
    #     #     6
    #     #    /  \
    #     #   3    12
    #     #  / \   / \
    #     # 1   4 9  14

    #     n1 = TreeNode(6)
    #     n2 = TreeNode(3)
    #     n3 = TreeNode(12)
    #     n4 = TreeNode(1)
    #     n5 = TreeNode(4)
    #     n6 = TreeNode(9)
    #     n7 = TreeNode(14)

    #     n1.left = n2
    #     n1.right = n3
    #     n2.left = n4
    #     n2.right = n5
    #     n3.left = n6
    #     n3.right = n7

    #     s = Solution()
    #     input_and_expected_outputs = [
    #         # (input1, input2, expected output) depending on number of arguments
    #         (n1, n6, n7, n3),
    #         (n1, n3, n5, n1),
    #         (n1, n4, n5, n1),  # Fail
    #     ]
    #     s = Solution()
    #     for input1, input2, input3, expected in input_and_expected_outputs:
    #         with self.subTest(input1=input1.val, input2=input2.val, input3=input3.val,
    #                           expected=expected.val):
    #             result = s.solve(input1, input2, input3)
    #             self.assertEqual(result, expected)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
