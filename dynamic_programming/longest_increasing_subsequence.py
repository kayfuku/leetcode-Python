# Author: leetcode + kei
# Date: October 17, 2022
import bisect
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    1. Dynamic Programming
    O(N^2) time, O(N) space.
    We store the max so far in the 'dp' array at the i-th element. And I can use
    that array to get the max at the current index i.
    For example, when the current index is 4, nums[i] is equal to 3.
    And while iterating through the dp array from index 0 to right before i, if
    nums[i] is bigger than the element that I am iterating in, then add 1 to the
    max at that point, and keep track of the max.
    Put the max in the dp array at the index i.
    ===i: 0 1 2 3 4 5 6
    nums:10 9 2 5 3 7 101

    ==dp: 1 1 1 2 2
    dp[3] = dp[2] + 1

    dp[i] = max(dp[j] + 1) (0 ≤ j < i)
    LIS = max(dp[i]) (0 ≤ i < n)
    '''

    def lengthOfLIS(self, nums: List[int]) -> int:
        # Since nums is unsorted, we need to keep track of max through
        # the dp array.
        # To hold the max values (longest) so far (index 0 to i).
        # dp[i] = max(dp[j] + 1) (0 ≤ j < i)
        dp = [1] * len(nums)
        # Fill up the dp assuming that nums[i] is the last element of the sequence.
        # i starts from 1 because no need to check when the list is just one element.
        for i in range(1, len(nums)):
            # Find max iterating through until i.
            for j in range(i):
                # Update dp only if nums[i] can be the last of the increasing subsequence.
                if nums[j] < nums[i]:
                    # Since nums[i] meets the requirement (increasing order),
                    # we can consider this is a candidate subsequence.
                    # nums[j] is the last element of that sequence.
                    # we count up the longest length so far (dp[j]) because
                    # dp[j] holds the longest length at the point of j.
                    # So, dp[j] + 1 is the length of that sequence and nums[i].
                    # We want the max among 0 <= j < i.
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


class Solution2:
    '''
    2. DP with Binary Search
    O(NlogN) time
    '''

    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            # bisect_left() returns index of num in sub if it's in sub.
            # Otherwise, it returns index at which num would be, which is
            # the index of the element that is smallest larger than num.
            i = bisect.bisect_left(sub, num)

            if i == len(sub):
                # num would be the last element, which is the largest in sub.
                # Note that elements in sub can change.
                sub.append(num)
            else:
                # Replace sub[i] that is smallest larger than (or equal to) num with num
                # because we will be able to use elements that are
                # greater than num but less than sub[i] in the future, which improves
                # on the length of increasing subsequence.
                # Note that sub is not always correct LIS, but it's ok because
                # we just need the maximum length.
                sub[i] = num

        return len(sub)


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_output = [
            # (input1, input2, expected output) depending on number of arguments
            ([10, 9, 2, 5, 3, 7, 101, 18], 4),
            ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),
        ]
        s = Solution()
        for case, (input1, expected) in enumerate(
                input_and_expected_output):
            print('Case: {}'.format(case))
            with self.subTest(input1=input1, expected=expected):
                result = s.lengthOfLIS(input1)
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
