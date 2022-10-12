# Author: leetcode + kei
# Date: October 8, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    '''

    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(first=0, curr=[]):
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, n):
                # (Partial candidate solution)
                curr.append(nums[i])
                # (Explore further)
                backtrack(i + 1, curr)
                # (Backtrack)
                curr.pop()

        output = []
        n = len(nums)
        # TODO: This might not be needed?
        for k in range(n + 1):
            backtrack()
        return output


class SolutionNG:
    '''
    NG! because it can't include [1, 3].
    '''

    def subsets_NG(self, nums: List[int]) -> List[List[int]]:

        def dfs(start=0):
            if start == n:
                return
            sol = []
            for i in range(start, n):
                sol.append(nums[i])
                ret.append(sol[:])
            dfs(start + 1)

        n = len(nums)
        ret = []
        dfs()
        return ret


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
