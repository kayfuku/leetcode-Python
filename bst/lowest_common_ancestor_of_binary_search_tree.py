# Author: leetcode + kei
# Date: July 18, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest

# In BST, we do not need to traverse all the nodes in the tree.


class Solution:
    '''
    Recursion
    '''

    def __init__(self):
        pass

    def lowestCommonAncestor(
            self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parent_val = root.val
        p_val = p.val
        q_val = q.val

        # Don't forget '=' here!
        if p_val <= parent_val and q_val >= parent_val or \
                p_val >= parent_val and q_val <= parent_val:
            # We have found the split point, i.e. the LCA node.
            return root

        if p_val > parent_val and q_val > parent_val:
            # Both p and q are greater than parent.
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < parent_val and q_val < parent_val:
            # Both p and q are less than parent.
            return self.lowestCommonAncestor(root.left, p, q)


class Solution2:
    '''
    Iteration
    '''

    def lowestCommonAncestor(
            self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_val = p.val
        q_val = q.val

        node = root
        while node:
            parent_val = node.val
            # Don't forget '=' here!
            if p_val <= parent_val and q_val >= parent_val or \
                    p_val >= parent_val and q_val <= parent_val:
                # We have found the split point, i.e. the LCA node.
                return node

            if p_val > parent_val and q_val > parent_val:
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                node = node.left


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
