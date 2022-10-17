# Author: leetcode + kei
# Date: October 17, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    1. Top-Down Dynamic Programming (Recursion + Memoization)
    O(N) time: totalWays gets called with each index from n to 3.
    Because of our memoization, each call will only take O(1)O(1) time.
    O(N) space because of the recursion stack all the way down until the
    base cases.
    '''

    def numWays(self, n: int, k: int) -> int:

        def total_ways(i):
            if i == 1:
                return k
            if i == 2:
                return k * k

            # Check if we have already calculated total_ways(i)
            if i in memo:
                return memo[i]

            # Use the recurrence relation to calculate total_ways(i)
            memo[i] = (k - 1) * (total_ways(i - 1) + total_ways(i - 2))
            return memo[i]

        memo = dict()
        return total_ways(n)


class Solution2:
    '''
    2. Bottom-Up Dynamic Programming (Tabulation)
    Good for interview
    O(N) time and space

    First, think about total_ways(1) and total_ways(2).
    total_ways(1) = k
    total_ways(2) = k * k

    Second, think about the recurrence relation.
    There are two options:
    1) Use a different color than the previous post
    total_ways_diff(i) => (k - 1) * total_ways(i - 1)

    2) Use the same color as the previous post
    We can paint the i-th post the same color as the (i - 1)-th post
    only if the (i - 1)-th post is a different color than the (i - 2)-th post.
    1 * total_ways_diff(i - 1) => (k - 1) * total_ways(i - 2)

    Therefore,
    total_ways(i) = (k - 1) * total_ways(i - 1) + (k - 1) * total_ways(i - 2)
                  = (k - 1) * (total_ways(i - 1) + total_ways(i - 2))

    '''

    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k

        total_ways = [0] * (n + 1)
        total_ways[1] = k
        total_ways[2] = k * k

        for i in range(3, n + 1):
            # Use the recurrence relation to calculate total_ways(i)
            total_ways[i] = (k - 1) * (total_ways[i - 1] + total_ways[i - 2])

        return total_ways[n]


class Solution3:
    '''
    3. Bottom-Up Dynamic Programming (Tabulation)
    O(N) time, O(1) space
    '''

    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k

        two_posts_back = k
        one_post_back = k * k

        for i in range(3, n + 1):
            # Use the recurrence relation to calculate total_ways(i)
            curr = (k - 1) * (one_post_back + two_posts_back)
            two_posts_back = one_post_back
            one_post_back = curr

        return curr


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
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
