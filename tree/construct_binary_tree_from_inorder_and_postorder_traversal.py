# Author: leetcode + kei
# Date: July 5, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest


class Solution:
    def __init__(self):
        pass

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # Use postorder to find the next root node, and use inorder and the root node
        # to figure out which nodes are in the left subtree or right subtree.

        def helper(in_left, in_right):
            if in_left > in_right:
                return None

            # The last element in the postorder list is a root.
            val = postorder.pop()
            root = TreeNode(val)

            # root splits inorder list
            # into left and right subtrees
            root_idx = in_idx_map[val]

            # Build right subtree first because the order of popping the root node
            # from the postorder list is right subtree first.
            root.right = helper(root_idx + 1, in_right)
            # build left subtree
            root.left = helper(in_left, root_idx - 1)

            return root

        # K: val, V: idx in inorder
        in_idx_map = {val: idx for idx, val in enumerate(inorder)}

        return helper(0, len(inorder) - 1)


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
    #     n1 = TreeNode(5)
    #     n2 = TreeNode(1)
    #     n3 = TreeNode(5)
    #     n4 = TreeNode(5)
    #     n5 = TreeNode(5)
    #     n6 = TreeNode(5)

    #     n1.left = n2
    #     n1.right = n3
    #     n3.right = n6
    #     n2.left = n4
    #     n2.right = n5

    #     s = Solution()
    #     result = s.solve(n1)
    #     self.assertEqual(result, 4)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
