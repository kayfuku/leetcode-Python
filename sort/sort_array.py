# Author: leetcode + kei
# Date: July 25, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    Insertion Sort is relatively important for interveiw
    O(N^2) time
    O(N) time for almost sorted list
    '''

    def sortArray(self, nums: List[int]) -> List[int]:
        '''
        TLE, but interviewers like this sorting algo.
        '''
        n = len(nums)
        for i in range(n):
            j = i
            while j - 1 >= 0 and nums[j - 1] > nums[j]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1

        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        # self.quickSort(nums)
        # self.mergeSort(nums)
        # self.bubbleSort(nums)
        self.insertionSort(nums)
        # self.selectionSort(nums)
        # self.heapSort(nums)
        return nums

    # @bubbleSort, TLE
    def bubbleSort(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

    # @insertionSort, TLE
    def insertionSort(self, nums):
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and nums[j] < key:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key

    # @selectionSort, TLE
    def selectionSort(self, nums):
        for i in range(len(nums)):
            _min = min(nums[i:])
            min_index = nums[i:].index(_min)
            nums[i + min_index] = nums[i]
            nums[i] = _min
        return nums

    # @quickSort
    def quickSort(self, nums):
        def helper(head, tail):
            if head >= tail:
                return
            l, r = head, tail
            m = (r - l) // 2 + l
            pivot = nums[m]
            while r >= l:
                while r >= l and nums[l] < pivot:
                    l += 1
                while r >= l and nums[r] > pivot:
                    r -= 1
                if r >= l:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
            helper(head, r)
            helper(l, tail)

        helper(0, len(nums)-1)
        return nums

        # @mergeSort
    def mergeSort(self, nums):
        if len(nums) > 1:
            mid = len(nums)//2
            L = nums[:mid]
            R = nums[mid:]

            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1

   # @heapSort
    def heapSort(self, nums):
        def heapify(nums, n, i):
            l = 2 * i + 1
            r = 2 * i + 2

            largest = i
            if l < n and nums[largest] < nums[l]:
                largest = l

            if r < n and nums[largest] < nums[r]:
                largest = r

            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]

                heapify(nums, n, largest)

        n = len(nums)

        for i in range(n//2+1)[::-1]:
            heapify(nums, n, i)

        for i in range(n)[::-1]:
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0)


class Solution2:
    '''
    Quicksort
    '''

    def sortArray(self, nums):
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, start, end):
        if end <= start:
            return

        mid = (start + end) // 2
        nums[start], nums[mid] = nums[mid], nums[start]
        i = start + 1
        j = end
        while i <= j:
            while i <= j and nums[i] <= nums[start]:
                i += 1
            while i <= j and nums[j] >= nums[start]:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        nums[start], nums[j] = nums[j], nums[start]
        self.quickSort(nums, start, j - 1)
        self.quickSort(nums, j + 1, end)


class Solution3:
    '''
    Sort an array in real life.
    '''

    def sortArray(self, nums):
        return sorted(nums)


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_outputs = [
            # (input1, input2, expected output) depending on number of arguments
            ([0, 1, 2], [0, 1, 2]),
            ([3, 1, 2, 5, 0], [0, 1, 2, 3, 5]),
            ([0], [0]),
            ([], []),
        ]
        s = Solution()
        for input1, expected in input_and_expected_outputs:
            with self.subTest(input1=input1, expected=expected):
                result = s.sortArray(input1)
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
