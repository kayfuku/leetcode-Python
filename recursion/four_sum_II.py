# Author: leetcode + kei
# Date: August 8, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest

from collections import defaultdict


class Solution:
    '''
    4 Sum solution
    '''

    def __init__(self):
        pass

    def fourSumCount(self,
                     A: List[int],
                     B: List[int],
                     C: List[int],
                     D: List[int]) -> int:
        cnt = 0
        m = defaultdict(int)
        # Get all the combinations of a and b.
        for a in A:
            for b in B:
                # Count the number that a and b add up to.
                m[a + b] += 1

        for c in C:
            for d in D:
                # If a number that c and d add up and multiplied by -1
                # is the same as the number we marked before, then
                # those are the tuple of four numbers that add up to zero.
                cnt += m[-(c + d)]

        return cnt


class Solution2:
    '''
    k Sum solution
    Cut recursion tree height in half so that we can save the time and space to
    square root of n^k.
    O(n^(k/2)) time and space
    '''

    def fourSumCount(
            self, A: List[int],
            B: List[int],
            C: List[int],
            D: List[int]) -> int:

        # initialized by 0 and can also avoid key error.
        m = defaultdict(int)
        lists = [A, B, C, D]

        def k_sum_count() -> int:
            # first half
            sum_first_half(0, 0)
            # second half
            return sum_second_half(len(lists) // 2, 0)

        def sum_first_half(i: int, total: int) -> None:
            if i == len(lists) // 2:
                m[total] += 1
                return
            # Sum all the combinations of the numbers of lists for first half.
            # We use recursion when the number of nested loops is a variable.
            for a in lists[i]:
                # One list of numbers at one recursion stack.
                sum_first_half(i + 1, total + a)

        def sum_second_half(i: int, total: int) -> int:
            if i == len(lists):
                # If the total is a complement of the total of the first half,
                # then it means that those numbers add up to zero.
                return m[-total]
            cnt = 0
            for a in lists[i]:
                cnt += sum_second_half(i + 1, total + a)
            return cnt

        return k_sum_count()


class Solution3:
    '''
    k Sum solution (TLE)
    O(n^k) time and space
    '''

    def fourSumCount(
            self, A: List[int],
            B: List[int],
            C: List[int],
            D: List[int]) -> int:

        lists = [A, B, C, D]

        def sum_all_comb(i: int, total: int) -> int:
            if i == len(lists):
                if total == 0:
                    return 1
                else:
                    return 0

            cnt = 0
            # Sum all the combinations of the numbers of lists for first half.
            for num in lists[i]:
                cnt += sum_all_comb(i + 1, total + num)

            return cnt

        return sum_all_comb(0, 0)


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
