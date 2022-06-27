# Author: leetcode + kei
# Date: May 10, 2022
import unittest
from typing import *
from helper_classes import *
import numpy as np


class Solution:
    def __init__(self):
        pass

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Recursive
        '''

        def dfs(node, postorder):
            if not node:
                return None

            dfs(node.left, postorder)
            dfs(node.right, postorder)
            postorder.append(node.val)

        ret = []
        dfs(root, ret)
        return ret


class Solution2:

    def __init__(self):
        pass

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Iterative
        Postorder is actually reversed Right-first-preorder.
        '''
        ret = []
        if not root:
            return ret

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            ret.insert(0, node.val)

            # Right-first-preorder.
            # Push left first so that you can pop right first.
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

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
        result = s.countUnivalSubtrees(n1)
        self.assertEqual(result, 4)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
