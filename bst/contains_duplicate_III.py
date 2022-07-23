# Author: leetcode + kei
# Date: July 18, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest

from sortedcontainers import SortedList, SortedSet


class Solution:
    '''
    1. Binary Search
    '''

    def __init__(self):
        pass

    def containsNearbyAlmostDuplicate(
            self, nums: List[int],
            k: int, t: int) -> bool:
        # SortedList is a sorted sequence where elems are maintained
        # in the sorted order.
        SList = SortedList()
        # Iterating the array, we use the sorted list as like a sorted
        # sliding window of size k.
        for i in range(len(nums)):
            # Add new element to the sorted list.
            SList.add(nums[i])
            if len(SList) == 1:
                continue
            if len(SList) > k + 1:
                # Remove the oldest element to maintain the size k.
                SList.remove(nums[i - (k + 1)])

            # Find the minimum greater than or equal to nums[i] in the sorted list.
            pred_idx = SList.bisect_left(nums[i])
            if pred_idx != 0 and abs(SList[pred_idx - 1] - nums[i]) <= t:
                return True

            # Find the maximum less than or equal to nums[i] in the sorted list.
            succ_idx = SList.bisect_left(nums[i])
            if succ_idx + 1 != len(SList) and \
                    abs(SList[succ_idx + 1] - nums[i]) <= t:
                return True

        return False


class Solution2:
    '''
    2. Bucket Sort (Not reviewed yet)
    '''

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        n = len(nums)
        buckets = {}
        w = t + 1
        for i in range(n):
            bucket_idx = nums[i] / w
            if bucket_idx in buckets:
                return True
            if bucket_idx - 1 in buckets and \
                    abs(nums[i] - buckets[bucket_idx - 1]) < w:
                return True
            if bucket_idx + 1 in buckets and \
                    abs(nums[i] - buckets[bucket_idx + 1]) < w:
                return True

            buckets[bucket_idx] = nums[i]
            if i >= k:
                del buckets[nums[i - k] / w]

        return False


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_outputs = [
            # (input1, input2, expected output) depending on number of arguments
            ([1, 0, 1, 1], 1, 2, True),
            ([1, 5, 9, 1, 5, 9], 2, 3, False),
        ]
        s = Solution2()
        for i, (input1, input2, input3, expected) in enumerate(
                input_and_expected_outputs):
            print(f"Test Case: {i+1}")
            with self.subTest(input1=input1, input2=input2, input3=input3, expected=expected):
                result = s.containsNearbyAlmostDuplicate(
                    input1, input2, input3)
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
