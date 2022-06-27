# Author: leetcode + kei
# Date: August 9, 2021
import unittest
from typing import *
from helper_classes import *


class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = 1
        if x < 0:
            x = -x
            sign = -1

        while x:
            pop = x % 10
            x //= 10
            if sign == 1:
                if rev > (pow(2, 31) - 1) // 10 or rev == (pow(2, 31) - 1) // 10 and pop > 7:
                    return 0
            else:
                if rev > pow(2, 31) // 10 or rev == pow(2, 31) // 10 and pop > 8:
                    return 0
            rev = rev * 10 + pop

        return rev if sign == 1 else rev * sign


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
