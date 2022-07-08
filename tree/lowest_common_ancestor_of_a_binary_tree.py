# Author: leetcode + kei
# Date: May 5, 2022
import unittest
from typing import *
from helper_classes import *
import numpy as np


class Solution:
    def __init__(self):
        pass

    def lowestCommonAncestor(
            self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Find p and q using DFS, then return candidate node.

        def recurse_tree(curr_node):
            if not curr_node or curr_node == p or curr_node == q:
                # No need to further explore this branch because
                # if the node is p or q, then the node can be the LCA even if there is
                # the other node in this brach.
                return curr_node

            left = recurse_tree(curr_node.left)
            right = recurse_tree(curr_node.right)

            if left and right:
                # Return the node when both child nodes are not null.
                return curr_node

            # Return not-null child node, and
            # return null if both nodes are null.
            return left if left else right

        lca = recurse_tree(root)

        return lca


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
            with self.subTest(input1=input1, input2=input2, input3=input3, expected=expected):
                result = s.lowestCommonAncestor(input1, input2, input3)
                self.assertEqual(result, expected)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
