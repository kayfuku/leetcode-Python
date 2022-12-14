# Author: leetcode + kei
# Date: December 14, 2022
from typing import *
from helper_classes import *
from collections import defaultdict, deque
from sortedcontainers import SortedList, SortedSet, SortedDict
import bisect
import heapq
import numpy as np
import unittest


class Solution:
    '''
    DP
    To think about recurrence relation,
    Let's look at an example costs = [0,1,2,3,4,5].
    Since we can take 1 or 2 steps at a time, we need to reach either step 4 or step 5 (0-indexed),
    and then pay the respective cost to reach the top. For this example,
    to reach step 4 optimally would cost 2 by taking path 0 --> 2 --> 4
    (we're not counting the cost of step 4 yet since we are only talking about
    reaching the step right now). To reach step 5 optimally would cost 4
    by taking path 1 --> 3 --> 5.

    Now, imagine that before we started the problem, somebody came up to us and
    said "to optimally reach step 4 costs 2 and to optimally reach step 5 costs 4."
    Well, then the problem is trivial - the answer is the minimum of 2 + cost[4] = 6
    and 4 + cost[5] = 9. The only reason this was so easy was because we already knew
    the cost to reach steps 4 and 5.
    '''

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, n + 1):
            # Recurrence relation
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[-1]

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        a = b = 0
        for i in range(2, len(cost) + 1):
            c = min(b + cost[i - 1], a + cost[i - 2])
            a = b
            b = c

        return c


class Try:
    '''
    WA!
    '''

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])
        dp = [0] * n
        dp[0] = cost[0]
        # NG!
        # dp[1] = min(cost[0], cost[1])
        # Since we must choose starting at 0 or 1, we can't take min of cost[0] and cost[1].
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i - 1], dp[i - 2] + cost[i])

        return dp[-1]


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
            ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
        ]
        s = Solution()
        for case, (input1, expected) in enumerate(
                input_and_expected_output):
            print('Case: {}'.format(case))
            with self.subTest(input1=input1, expected=expected):
                # Change to the method name to be tested.
                result = s.minCostClimbingStairs(input1)
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
