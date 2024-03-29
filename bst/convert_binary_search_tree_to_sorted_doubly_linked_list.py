# Author: leetcode + kei
# Date: August 3, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    Two pointers
    '''

    def __init__(self):
        pass

    def treeToDoublyList(self, root: Node) -> Node:

        def helper(curr):
            """
            Performs standard inorder traversal:
            left -> curr -> right
            and links all nodes into DLL
            """
            # This is needed.
            nonlocal head, tail
            if curr is None:
                return

            # In-order traversal ('curr' will be accessed in in-order order in the BST)
            # 1. left
            helper(curr.left)
            # 2. curr
            if tail:
                # Link the previous node (tail) with the current one (curr).
                tail.right = curr
                curr.left = tail
            else:
                # Keep the smallest node to close DLL later on.
                head = curr

            # Move the tail node to the current node.
            tail = curr
            # 3. right
            helper(curr.right)

        if not root:
            return None

        head, tail = None, None
        helper(root)

        # Close DLL.
        tail.right = head
        head.left = tail

        return head


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
