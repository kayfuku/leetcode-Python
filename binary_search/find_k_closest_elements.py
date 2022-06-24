# Author: leetcode + kei
# Date: May 15, 2022
import unittest
from typing import *
from helper_classes import *
import numpy as np


class Solution:
    def __init__(self):
        pass

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        The list we want is [A1, A2, ... x, ... Ak] (len: k).
        Using Binary Search, we're going to find A1.
        Pick up a 'mid' and check if the condition is met.
        'mid' is our attempt to find A1.
        Be careful that x cannot be in the list, and the distance is not defined
        by indices of the list. Also, there can be duplicate numbers in the list.
        ex)
        arr: [0,0,1,2,3,3,4,7,7,8]
        k: 3
        x: 5
        => return [3,3,4]
        We need to keep searching to find leftmost.
        '''
        # Possible bounds of A1
        left = 0
        right = len(arr) - k
        while left <= right:
            mid = (left + right) // 2
            A = x - arr[mid]
            if mid + k == len(arr):
                # Avoid out of bound.
                return arr[mid:]
            B = arr[mid + k] - x
            if A <= B:
                # Search left side.
                right = mid - 1
            else:
                left = mid + 1

        return arr[left:left + k]


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
