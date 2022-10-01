# Author: leetcode + kei
# Date: September 27, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    Binary Search (to find leftmost)
        Taking capacity (equivalent to index for normal Binary Search) as the
        horizontal axis and days needed as the vertical axis, if capacity increases,
        then days needed decreases. Therefore, capacity and days needed form
        a monotonically non-increasing curve. The reason of non-increasing is
        because even if capacity increases a little, days needed might not change.
        Binary Search can be used on that curve.
    '''

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # The min capacity for left.
        # The max capacity for right.
        min_capacity = max(weights)  # O(N) time
        max_capacity = sum(weights)  # O(N) time
        while min_capacity <= max_capacity:
            # mid
            capacity = min_capacity + (max_capacity - min_capacity) // 2
            # Monotonically non-increasing function that takes as input capacity
            # and returns days needed. The smaller the capacity, the more days it takes.
            days_needed = self.get_days(capacity, weights)
            # Note that even if we find days_needed that equals to the given days,
            # there might be less cacpacity than that to meet the requirement.
            # (find leftmost pattern)
            if days_needed <= days:
                # Search for less capacity.
                max_capacity = capacity - 1
            else:
                min_capacity = capacity + 1

        # Return left
        return min_capacity

    def get_days(self, capacity, weights):
        # O(N) time
        days_needed = 1
        sum = 0
        for p in weights:
            sum += p
            if sum > capacity:
                days_needed += 1
                # Don't forget this package, not 0 here.
                sum = p

        return days_needed


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_output = [
            # (input1, input2, expected output) depending on number of arguments
            ([1, 2, 3, 1, 1], 4, 3),
        ]
        s = Solution()
        for case, (input1, input2, expected) in enumerate(
                input_and_expected_output):
            print('Case: {}'.format(case))
            with self.subTest(input1=input1, input2=input2, expected=expected):
                result = s.shipWithinDays(input1, input2)
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
