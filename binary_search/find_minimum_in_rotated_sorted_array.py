# Author: leetcode + kei
# Date: September 19, 2021, September 25, 2022
import unittest
from typing import *
from helper_classes import *
import numpy as np


class Solution:

    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[len(nums) - 1]:
            # The last element is greater than the first element then there is no rotation.
            # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
            # Hence the smallest element is first element. A[0]
            return nums[0]

        # Binary search way
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            # TODO:
            # Check if the nums[mid] is the minimum.
            # If the left neighbor is bigger than the nums[mid], then
            # nums[mid] is the minimum.
            # Be careful if the mid is 0.
            # The reason we need the second condition is because with the R = M-1 version of
            # binary search, the mid can move like index 2 -> 0 -> 1. In that case,
            # we check index 0 before index 1. If the elem at index 1 is the minimum,
            # then we need,
            # 'nums[mid] < nums[mid + 1]'
            # to continue when the mid is equal to 0.

            # if mid != 0 and nums[mid - 1] > nums[mid] or \
            #    mid == 0 and nums[mid] < nums[mid + 1]:
            if mid != 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return -1


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
