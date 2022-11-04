# Author: lee215 + kei
# Date: June 21, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest

from collections import Counter


class Solution:
    '''
    O(2^n) time and space, where n is the A length.
    '''

    def findTargetSumWays(self, A, S):
        # Use Counter because we can handle negative numbers as intermediate amount.
        # Initialize with 0 as key and its count 1 as value.
        count = Counter({0: 1})
        for x in A:
            count_updated = Counter()
            # 'count' is the previous 'count_updated' which keeps track of the number of
            # ways for each key.
            for y in count:
                # y + x and y - x take over the number of ways for y.
                count_updated[y + x] += count[y]
                count_updated[y - x] += count[y]

            count = count_updated

        return count[S]


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_outputs = [
            # (input1, input2, expected output) depending on number of arguments
            ([10, 5, 5], 10, 3),  # Fail
            ([10, 5, 5], 10, 2),
        ]
        s = Solution()
        for input1, input2, expected in input_and_expected_outputs:
            with self.subTest(input1=input1, input2=input2, expected=expected):
                result = s.findTargetSumWays(input1, input2)
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
