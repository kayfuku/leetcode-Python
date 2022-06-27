# Author: leetcode + kei
# Date: May 9, 2022
import unittest
from typing import *
from helper_classes import *
import numpy as np


class Solution:

    def __init__(self):
        pass

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Recursive
        '''

        def dfs(node, preorder):
            if not node:
                return None

            preorder.append(node.val)
            dfs(node.left, preorder)
            dfs(node.right, preorder)

        ret = []
        dfs(root, ret)
        return ret


class Solution2:

    def __init__(self):
        pass

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Iterative
        '''
        ret = []
        if not root:
            return ret

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            ret.append(node.val)

            # Add all the children of the node to stack.
            # Note that right child is first, then left for pre-order traversal.
            # When popped, left child first.
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return ret


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

    def test_tree(self):
        '''
        Tree test example
        '''
        n1 = TreeNode(5)
        n2 = TreeNode(1)
        n3 = TreeNode(5)
        n4 = TreeNode(5)
        n5 = TreeNode(5)
        n6 = TreeNode(5)

        n1.left = n2
        n1.right = n3
        n3.right = n6
        n2.left = n4
        n2.right = n5

        s = Solution()
        result = s.solve(n1)
        self.assertEqual(result, 4)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
