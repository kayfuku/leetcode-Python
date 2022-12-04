# Author: leetcode + kei
# Date: December 4, 2022
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
    Union Find
    Note: The important point to note here is that if we have pairs like (a, b) and (b, c),
    then we can swap characters at indices a and c. Although we don't have the pair (a, c),
    we can still swap them by first swapping them with the character at index b.
    Thus, because we can swap the characters at these indices any number of times,
    we can rearrange the characters a, b, and c into any order.
    '''

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        class UF:

            def __init__(self, n):
                self.p = list(range(n))

            def find(self, x):
                if x == self.p[x]:
                    return x
                self.p[x] = self.find(self.p[x])
                return self.p[x]

            def unite(self, x, y):
                # No need to check if x and y are in the same group for this problem.
                self.p[self.find(x)] = self.find(y)

        # Create a graph with union find.
        uf = UF(len(s))
        for x, y in pairs:
            uf.unite(x, y)

        # Group the characters at the indices which belong to the same group.
        # K: root, V: list of nodes in the same group
        m = defaultdict(list)
        for i in range(len(s)):
            root = uf.find(i)
            m[root].append(s[i])

        for comp_id in m.keys():
            m[comp_id].sort(reverse=True)

        res = []
        for i in range(len(s)):
            res.append(m[uf.find(i)].pop())

        return ''.join(res)


class Try:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        return 0


class Cbase:

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
