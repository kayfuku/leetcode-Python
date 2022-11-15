# Author: leetcode + kei
# Date: May 11, 2022
import unittest
from typing import *
from helper_classes import *
import numpy as np
import bisect


class Solution:

    def search1(self, nums: List[int], target: int) -> int:
        '''
        1. Binary Search
        Find x, return -1 if x is not in the list.
        '''
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def search2(self, nums: List[int], target: int) -> int:
        '''
        2. Binary Search (Basic)
        Find x, 'left' is a possible index of x.
        '''
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        # 'left' is a possible index of x.
        return left

    def search3(self, nums: List[int], target: int) -> int:
        '''
        3. Built-in Binary Search (Basic)
        Find x, 'left' is a possible index of x.
        '''
        return bisect.bisect_left(nums, target)

    def search4(self, nums: List[int], target: int) -> int:
        '''
        4. Binary Search (leftmost)
        Find leftmost x.
        '''
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        # 'left' is the leftmost index or the index at which 'x' would be.
        # ('right' is the index for largest smaller than x)
        return left

    def search5(self, nums: List[int], target: int) -> int:
        '''
        5. Binary Search (largest smaller)
        Find rightmost largest smaller than x.
        '''
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        # 'right' is the 'rightmost largest smaller' index or the index at which it would be.
        return right

    def search6(self, nums: List[int], target: int) -> int:
        '''
        6. Binary Search (rightmost)
        Find rightmost x. Be careful when x is not in the list.
        '''
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        # If 'x' is in the list, 'right' ( or 'left - 1') is the rightmost index.
        # If 'x' is not in the list, 'right + 1' ( or 'left') is the index at which 'x' would be.
        # ('left' is also the index for smallest larger than x)
        return right

    def search7(self, nums: List[int], target: int) -> int:
        '''
        7. Binary Search (smallest larger)
        Find leftmost smallest larger than x.
        '''
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        # 'left' is the 'leftmost smallest larger' index or the index at which it would be.
        return left

    def search8(self, nums: List[int], target: int) -> int:
        '''
        8. Built-in Binary Search (smallest larger)
        '''
        return bisect.bisect_right(nums, target)


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_outputs = [
            # (input1, input2, expected output) depending on number of arguments
            # [1] Binary Search
            # ([0, 1, 3, 5, 7], 5, 3),
            # ([0, 1, 3, 5, 7], 6, -1),
            # ([0, 1, 3, 5, 7], 8, -1),
            # [2, 3] Binary Search (Basic)
            # Find x, "left" is a possible index of x.
            # ([0, 1, 3, 5, 7], 5, 3),
            # ([0, 1, 3, 5, 7], 6, 4),
            # ([0, 1, 3, 5, 7], 8, 5),  # Caution!
            # [4] Binary Search (leftmost)
            # ([0, 1, 1, 1, 5], 1, 1),
            # ([0, 0, 1, 1, 5], 0, 0),
            # ([3, 3, 3, 3, 3], 3, 0),
            # ([0, 2, 4, 5, 7], 3, 2),
            # ([0, 2, 4, 5, 7], 8, 5),  # Caution!
            # [5] Binary Search (largest smaller)
            # ([0, 2, 4, 5, 7], 4, 1),
            # ([0, 2, 3, 3, 7], 3, 1),
            # ([2, 2, 3, 3, 7], 3, 1),
            # ([3, 3, 3, 3, 7], 3, -1),  # Caution!
            # ([0, 2, 4, 5, 7], 3, 1),
            # ([0, 2, 4, 5, 7], 8, 4),
            # [6] Binary Search (rightmost)
            # ([0, 1, 1, 1, 5], 1, 3),
            # ([0, 1, 1, 5, 5], 5, 4),
            # ([3, 3, 3, 3, 3], 3, 4),
            # ([0, 2, 4, 5, 7], 3, 1),  # Caution!
            # ([0, 2, 4, 5, 7], 8, 4),  # Caution!
            # [7, 8] Binary Search (smallest larger)
            ([0, 2, 4, 5, 7], 4, 3),
            ([0, 3, 3, 7, 7], 3, 3),
            ([1, 2, 3, 3, 3], 3, 5),  # Caution!
            ([0, 2, 4, 5, 7], 3, 2),
            ([0, 2, 4, 5, 7], 8, 5),  # Caution!

        ]
        s = Solution()
        for input1, input2, expected in input_and_expected_outputs:
            with self.subTest(input1=input1, input2=input2, expected=expected):
                result = s.search8(input1, input2)
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
