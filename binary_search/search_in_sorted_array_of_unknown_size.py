# Author: leetcode + kei
# Date: May 18, 2022
from turtle import left
from typing import *
from helper_classes import *
import numpy as np
import unittest
import abc


class Solution:
    def __init__(self):
        pass

    def search(self, reader: 'ArrayReader', target: int) -> int:
        # Find search space to use Binary Search.
        right = 1
        while reader.get(right) < target:
            right = right << 1
        left = right >> 1

        # Binary Search
        while left <= right:
            mid = (left + right) // 2
            if reader.get(mid) == target:
                return mid
            if reader.get(mid) > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1


class ArrayReader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, index: int) -> int:
        raise NotImplementedError()


class TestCalc(unittest.TestCase):

    def test_solve(self):
        '''
        For more than one argument
        For one argument, comment out some lines.
        '''
        input_and_expected_outputs = [
            # ((input), expected output) or
            # (input, expected output)
            (([0, 1, 2], 3), 6),
            (([0, 1], 3), 5),
        ]
        s = Solution()
        for input, expected in input_and_expected_outputs:
            # result = s.solve(input)
            result = s.solve(*input)
            self.assertEqual(result, expected)


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
