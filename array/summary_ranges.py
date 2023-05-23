# Author: leetcode + kei
# Date: May 23, 2023
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
    '''
    '''

    def summaryRanges(self, nums: List[int]) -> List[str]:
        '''
        Two pointers
        '''
        if not nums:
            return []
        res = []
        i = 0
        while i < len(nums):
            start = nums[i]
            # See how nicer it handles than for loop.
            # You can find end before accessing nums[i+1] (out of bound).
            while i + 1 < len(nums) and nums[i] + 1 == nums[i+1]:
                i += 1
            end = nums[i]
            if start != end:
                res.append("{}->{}".format(start, end))
            else:
                res.append(str(end))
            i += 1

        return res


class Try:

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ans = []
        N = len(nums)
        # [0,1,2,4,5,7]
        start = nums[0]
        # The comparison like this can cause a duplicate code after the for loop
        # because you can't access nums[i+1] (out of bound).
        for i in range(N):
            if nums[i] - nums[i-1] > 1:
                end = nums[i-1]
                if end == start:
                    ans.append(str(end))
                else:
                    ans.append("{}->{}".format(start, end))

                start = nums[i]

        end = nums[N-1]
        if end == start:
            ans.append(str(end))
        else:
            ans.append("{}->{}".format(start, end))

        return ans


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
