# Author: leetcode + kei
# Date: October 8, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    Since we don't know how many elements in one group, recursion is useful for this problem.
    Think of a recursion tree, where nodes are the subsets consists of nums[i].
    Pick one element and go further using that element.
    Or, pick another element to the right of current one by backtraking.
    '''

    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(start=0):
            if start == n:
                # Stop going further.
                return

            # Pick every element to the right of 'start' until the last element.
            for i in range(start, n):
                # (Partial candidate solution)
                curr_subset.append(nums[i])

                # Create a new list of curr_subset and put it in the output.
                output.append(curr_subset[:])

                # For each recursion stack, the size grows by one.
                # Prior to the 'start' index, those elements has been already used,
                # so start from 'start', which is the next possible element.
                # (Explore further)
                backtrack(i + 1)

                # When we come back from lower recursion stack, we undo the adding to
                # replace the last element with the next element. (Backtrack)
                curr_subset.pop()

        n = len(nums)
        output = []
        output.append([])
        curr_subset = []
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
