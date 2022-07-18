# Author: leetcode + kei
# Date: July 17, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    1. Use inorder successor and predecessor
    '''

    def __init__(self):
        pass

    def get_inorder_successor(self, root):
        # One step right and then always left
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def get_inorder_predecessor(self, root):
        # One step left and then always right
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not (root.left or root.right):
                # the node is a leaf
                root = None
            elif root.right:
                # the node is not a leaf and has a right child
                root.val = self.get_inorder_successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                # the node is not a leaf, has no right child, and has a left child
                root.val = self.get_inorder_predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root


class Solution2:
    '''
    2. No need to get a predecessor
    '''

    def __init__(self):
        pass

    def get_inorder_successor(self, root):
        # One step right and then always left
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None

        if key == root.val:
            # 1. No child node or One child node
            # Replace the current node with None or its child node.
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            # 2. Two child nodes
            # Replace the current node with its inorder successor.
            # Copy the inorder successor val to the current node val.
            root.val = self.get_inorder_successor(root)
            # Delete the inorder successor in the right subtree.
            root.right = self.deleteNode(root.right, root.val)

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)

        return root


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
