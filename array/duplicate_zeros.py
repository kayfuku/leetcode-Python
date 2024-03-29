# Author: leetcode + kei
# Date: August 24, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    First, think about copy to another array. Then, think about copy in-place.
    '''

    def __init__(self):
        pass

    def duplicateZeros(self, arr: List[int]) -> None:
        # The number of zeroes in the array, which is a maximum shift distance.
        # Shift distance is equal to the number of zeroes to the left of each element.
        shift = arr.count(0)
        n = len(arr)
        # Start copying from the last element so that we don't overwrite
        # the values we need.
        for i in range(n - 1, -1, -1):
            # We can't copy at index out of bound.
            if i + shift < n:
                # Copy in-place.
                # Basically, we copy each element whether it's zero or not.
                arr[i + shift] = arr[i]
            if arr[i] == 0:
                # Decrement shift distance by one.
                shift -= 1
                if i + shift < n:
                    # Copy the zero again.
                    arr[i + shift] = 0


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_outputs = [
            # (input1, input2, expected output) depending on number of arguments
            ([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]),
            ([1, 0, 2, 3, 0, 0, 5, 0], [1, 0, 0, 2, 3, 0, 0, 0]),
        ]
        s = Solution()
        for input1, expected in input_and_expected_outputs:
            with self.subTest(input1=input1, expected=expected):
                s.duplicateZeros(input1)
                self.assertEqual(input1, expected)

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
