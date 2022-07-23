# Author: leetcode + kei
# Date: July 23, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    Balanced =>
    1. left subtree and right subtree are balanced and
    2. height of left subtree and height of right subtree differ by
    no more than one.
    '''

    def __init__(self):
        pass

    def get_height(self, node):
        if node is None:
            return -1

        h_left = self.get_height(node.left)
        h_right = self.get_height(node.right)
        h = max(h_left, h_right) + 1
        return h

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        # 1. left subtree and right subtree are balanced.
        is_left_balanced = self.isBalanced(root.left)
        is_right_balanced = self.isBalanced(root.right)
        if not is_left_balanced or not is_right_balanced:
            return False

        # 2. The heights of both subtrees differ by no more than one.
        h_left = self.get_height(root.left)
        h_right = self.get_height(root.right)
        if abs(h_left - h_right) > 1:
            return False

        return True


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

        n1 = TreeNode(6)
        n2 = TreeNode(3)
        n3 = TreeNode(12)
        n4 = TreeNode(1)
        n5 = TreeNode(4)
        n6 = TreeNode(9)
        n7 = TreeNode(14)

        n1.left = n2
        n1.right = n3
        n2.left = n4
        n2.right = n5
        n3.left = n6
        n3.right = n7

        s = Solution()
        input_and_expected_outputs = [
            # (input1, input2, expected output) depending on number of arguments
            (n1, n6, n7, n3),
            (n1, n3, n5, n1),
            (n1, n4, n5, n1),  # Fail
        ]
        s = Solution()
        for input1, input2, input3, expected in input_and_expected_outputs:
            with self.subTest(input1=input1.val, input2=input2.val, input3=input3.val,
                              expected=expected.val):
                result = s.solve(input1, input2, input3)
                self.assertEqual(result, expected)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
