# Author: leetcode + kei
# Date: November 5, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    myPow = pow


class Solution2:
    def myPow(self, x, n):
        return x ** n


class Solution3:
    '''
    Recursive
    O(logN) time and space
    '''

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)

        return self.myPow(x * x, n / 2)


class Solution4:
    '''
    Iterative
    ex) x^21 = 2^0 + 2^2 + 2^4
    x: 10101
    10101 = 00001 + 00100 + 10000
    - shift
    01010
    00101
    00010
    00001
    00000

    O(logN) time, O(1) space
    '''

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        pow = 1
        while n:
            if n & 1:
                # Multiply the result so far when LSB of n is 1.
                pow *= x

            # Double the number of times to multiply x.
            x *= x
            # Shift to the right by one bit.
            n >>= 1

        return pow


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
