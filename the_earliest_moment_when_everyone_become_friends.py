# Author: leetcode + kei
# Date: November 28, 2022
from typing import *
from helper_classes import *
from collections import *
from sortedcontainers import SortedList, SortedSet, SortedDict
import heapq
import numpy as np
import unittest


class Solution:
    '''
    Union Find
    '''

    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # First, we need to sort the events in chronological order.
        logs.sort(key=lambda x: x[0])

        uf = UnionFind(n)
        # Initially, we treat each individual as a separate group.
        group_cnt = n

        # We merge the groups along the way.
        for timestamp, friend_a, friend_b in logs:
            if not uf.is_same(friend_a, friend_b):
                uf.unite(friend_a, friend_b)
                group_cnt -= 1

            # The moment when all individuals are connected to each other.
            if group_cnt == 1:
                return timestamp

        # There are still more than one groups left,
        # i.e. not everyone is connected.
        return -1


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
