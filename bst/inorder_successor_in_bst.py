# Author: leetcode + kei
# Date: July 11, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    '''

    def __init__(self):
        pass

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        # Just memorize it.

        successor = None
        node = root
        while node:
            if node.val <= p.val:
                # Go right.
                node = node.right
            else:
                # p.val < node.val
                # Go left.
                # Keep the node as a successor candidate.
                successor = node
                node = node.left

        return successor


class TestSolution(unittest.TestCase):

    # def test_solve(self):
    #     '''
    #     Test
    #     '''
    #     input_and_expected_outputs = [
    #         # (input1, input2, expected output) depending on number of arguments
    #         ([0, 1, 2], 3, 6),
    #         ([0, 1], 3, 5),
    #     ]
    #     s = Solution()
    #     for input1, input2, expected in input_and_expected_outputs:
    #         with self.subTest(input1=input1, input2=input2, expected=expected):
    #             result = s.solve(input1, input2)
    #             self.assertEqual(result, expected)

    def test_tree(self):
        '''
        Tree test example
        '''
        # Binary Tree
        #     6
        #    /  \
        #   3    12
        #  / \   / \
        # 1   4 9  14

        n6 = TreeNode(6)
        n3 = TreeNode(3)
        n12 = TreeNode(12)
        n1 = TreeNode(1)
        n4 = TreeNode(4)
        n9 = TreeNode(9)
        n14 = TreeNode(14)

        n6.left = n3
        n6.right = n12
        n3.left = n1
        n3.right = n4
        n12.left = n9
        n12.right = n14

        s = Solution()
        input_and_expected_outputs = [
            # (input1, input2, expected output) depending on number of arguments
            (n6, n4, n6),
            (n6, n6, n9),
            (n6, n3, n4),
        ]
        s = Solution()
        for input1, input2, expected in input_and_expected_outputs:
            with self.subTest(input1=input1.val, input2=input2.val, expected=expected.val):
                result = s.inorderSuccessor(input1, input2)
                self.assertEqual(result, expected)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
