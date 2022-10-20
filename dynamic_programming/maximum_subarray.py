# Author: leetcode + kei
# Date: August 9, 2021, October 18, 2022
from re import I
from tracemalloc import start
import unittest
from typing import *
from helper_classes import *


class Solution:
    '''
    Dynamic Programming
    '''

    def maxSubArray(self, nums: List[int]) -> int:
        # For keeping track of contiguous subarray max.
        # Do not set it to 0 because the elements and max can be negative!
        # Do not set it to int('inf') because curr_sum + num could overflow!
        curr_sum = max_sum = nums[0]

        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If curr_sum is negative, throw it away. Otherwise, keep adding to it.
            curr_sum = max(num, curr_sum + num)
            # Take max of curr_sum.
            max_sum = max(max_sum, curr_sum)

        return max_sum

    def maxSubArray2(self, nums: List[int]) -> int:
        # For keeping track of contiguous subarray max.
        # Do not set it to 0 because the elements and max can be negative!
        # Do not set it to int('inf') because curr_sum + num could overflow!
        curr_sum = max_sum = nums[0]
        start = end = 0  # optional

        # Start with the 2nd element since we already used the first one.
        for i in range(1, len(nums)):
            # If curr_sum is negative, throw it away. Otherwise, keep adding to it.
            # curr_sum + nums[i] is for the sum of contiguous subarray.
            # TODO: Think more about it.
            if nums[i] > curr_sum + nums[i]:
                # nums[i] itself is bigger than the previous contiguous subarray
                # nums[i] is the restart of contiguous subarray.
                # curr_sum = max(curr_sum + nums[i], nums[i]);
                curr_sum = nums[i]
                start = i  # optional
            else:
                curr_sum = curr_sum + nums[i]

            # Take max of curr_sum.
            if curr_sum > max_sum:
                max_sum = curr_sum
                end = i  # optional

        print("start: {}, end: {}".format(start, end))
        return max_sum


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_outputs = [
            # (input1, input2, expected output) depending on number of arguments
            ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([-2, 1, -3, 4, -1], 4),
            ([-2, 1, -3], 1),
        ]
        s = Solution()
        for input1, expected in input_and_expected_outputs:
            with self.subTest(input1=input1, expected=expected):
                result = s.maxSubArray2(input1)
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
