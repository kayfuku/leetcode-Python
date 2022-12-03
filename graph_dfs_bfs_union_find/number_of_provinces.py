# Author: leetcode + kei
# Date: December 3, 2022
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
    1. Union Find
    '''

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        '''
        TODO:
        '''
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    uf.unite(i, j)

        return uf.get_number_of_groups()

    def findCircleNum_NG(self, isConnected: List[List[int]]) -> int:
        '''
        NG if there is a cycle.
        '''
        n = len(isConnected)
        num_group = n
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    uf.unite(i, j)
                    num_group -= 1

        return num_group


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        Change input and expected output as needed.
        '''
        input_and_expected_output = [
            # (input1, input2, expected output) depending on number of arguments
            ([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]], 1),
        ]
        s = Solution()
        for case, (input1, expected) in enumerate(
                input_and_expected_output):
            print('Case: {}'.format(case))
            with self.subTest(input1=input1, expected=expected):
                # Change to the method name to be tested.
                result = s.findCircleNum(input1)
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
