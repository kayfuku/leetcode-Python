# Author: leetcode + kei
# Date: November 20, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    '''

    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        # Find the first element from the end to the left where nums[i] < nums[i + 1].
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Find next smallest larger than nums[i].
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap.
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse sort the list to the right of i in place.
        self.reverse(nums, i + 1)

    def reverse(self, nums, start):
        i = start
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        Change input and expected output as needed.
        '''
        input_and_expected_output = [
            # (input1, input2, expected output) depending on number of arguments
            ([1, 2, 3], [1, 3, 2]),
            ([3, 2, 1], [1, 2, 3]),
        ]
        s = Solution()
        for case, (input1, expected) in enumerate(
                input_and_expected_output):
            print('Case: {}'.format(case))
            with self.subTest(input1=input1, expected=expected):
                # Change to the method name to be tested.
                result = s.nextPermutation(input1)
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
