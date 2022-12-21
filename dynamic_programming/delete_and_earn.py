# Author: leetcode + kei
# Date: December 17, 2022
from typing import *
from helper_classes import *
from collections import defaultdict, deque
from sortedcontainers import SortedList, SortedSet, SortedDict
import bisect
import heapq
import numpy as np
from functools import cache
import unittest


class Solution:

    def deleteAndEarn(self, nums: List[int]) -> int:
        '''
        Bottom-Up DP
        Good for interview
        '''
        # K: num, V: points
        points = defaultdict(int)
        max_num = 0
        # Precompute how many points we gain from taking an element.
        for num in nums:
            points[num] += num
            max_num = max(max_num, num)

        dp = [0] * (max_num + 1)
        dp[1] = points[1]
        for num in range(2, len(dp)):
            # Recurrence relation
            # dp[num]: maximum points when we take num
            dp[num] = max(dp[num - 1], dp[num - 2] + points[num])

        return dp[max_num]

    def deleteAndEarn2(self, nums: List[int]) -> int:
        '''
        Top-Down DP
        '''
        points = defaultdict(int)
        max_num = 0
        # Precompute how many points we gain from taking an element
        for num in nums:
            points[num] += num
            max_num = max(max_num, num)

        @cache
        def max_points(num):
            if num == 0:
                return 0
            if num == 1:
                return points[1]

            # Recurrence relation
            return max(max_points(num - 1), max_points(num - 2) + points[num])

        return max_points(max_num)


class Try:

    def deleteAndEarn(self, nums: List[int]) -> int:
        num_to_points = defaultdict(int)
        for num in range(nums):
            num_to_points[num] += num

        return 0


class Bot:

    def solve(self, nums: List[int], target: int) -> List[int]:
        return 0


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        Change input and expected output as needed.
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
                # Change to the method name to be tested.
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
