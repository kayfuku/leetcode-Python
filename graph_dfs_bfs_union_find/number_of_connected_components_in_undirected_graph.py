# Author: leetcode + kei
# Date: September 17, 2022
from gettext import find
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    Union Find
    '''

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # First, every node is isolated. The number of group is n at first.
        uf = UnionFind(n)
        for u, v in edges:
            uf.unite(u, v)

        return uf.get_number_of_groups()

    def countComponents2(self, n: int, edges: List[List[int]]) -> int:
        # First, every node is isolated. The number of group is n at first.
        uf = UF(n)
        # Next, unite nodes that are connected and decrement n by one.
        for u, v in edges:
            if uf.unite(u, v):
                n -= 1
        return n


class UF:

    def __init__(self, n) -> None:
        self.roots = [i for i in range(n)]

    def find(self, x):
        if self.roots[x] == x:
            return self.roots[x]
        # self.roots[x] = self.find(self.roots[x])
        return self.find(self.roots[x])

    def unite(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        self.roots[root_x] = root_y
        return True


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_output = [
            # (input1, input2, expected output) depending on number of arguments
            ([[0, 1], [0, 2], [1, 2], [2, 3], [2, 4]], 1),
        ]
        s = Solution()
        for case, (input1, expected) in enumerate(
                input_and_expected_output):
            print('Case: {}'.format(case))
            with self.subTest(input1=input1, expected=expected):
                result = s.countComponents(len(input1), input1)
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
