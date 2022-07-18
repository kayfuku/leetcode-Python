# Author: leetcode + kei
# Date: July 12, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    Iterative
    '''

    def __init__(self):
        pass

    def searchBST(
            self, root: Optional[TreeNode],
            val: int) -> Optional[TreeNode]:
        node = root
        while node:
            if node.val == val:
                return node

            # Don't make a mistake like using '>' here again!
            # Think of val as target.
            if node.val < val:
                # Go search on the right.
                node = node.right
            else:
                node = node.left

        return node


class Solution2:
    '''
    Recursive
    '''

    def __init__(self):
        pass

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return root
        if root.val == val:
            return root

        # This is just my personal preference, but easier to debug.
        ret = None
        if root.val > val:
            ret = self.searchBST(root.left, val)
        else:
            ret = self.searchBST(root.right, val)

        return ret

        # # Tail recursion is more efficient for time and space.
        # return self.searchBST(root.left, val) if val < root.val \
        #     else self.searchBST(root.right, val)


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
        #     4
        #    /  \
        #   2    7
        #  / \
        # 1   3

        n1 = TreeNode(4)
        n2 = TreeNode(2)
        n3 = TreeNode(7)
        n4 = TreeNode(1)
        n5 = TreeNode(3)

        n1.left = n2
        n1.right = n3
        n2.left = n4
        n2.right = n5

        s = Solution()
        input_and_expected_outputs = [
            # (input1, input2, expected output) depending on number of arguments
            (n1, 2, n2),
            (n1, 1, n4),
            (n1, 3, n5),
        ]
        s = Solution()
        for input1, input2, expected in input_and_expected_outputs:
            with self.subTest(input1=input1.val, input2=input2, expected=expected.val):
                result = s.searchBST(input1, input2)
                self.assertEqual(result, expected)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
