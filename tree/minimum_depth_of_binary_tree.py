# Author: leetcode + kei
# Date: July 21, 2021, September 7, 2022
import unittest
from typing import *
from helper_classes import *


class Solution:
    '''
    1. DFS recursive
    If the node has only one child, we can't just take minimum of two
    subtrees' heights.
    '''

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left_subtree = self.minDepth(root.left)
        right_subtree = self.minDepth(root.right)

        # If node has only one child, then the depth is 2, not 1.
        # So we can't just take minimum of two subtrees' heights.
        # left == | right == | depth == |
        # null(0) | not null | right + 1
        # not null| null(0)  | left + 1
        # null(0) | null(0)  | 1
        if root.left is None or root.right is None:
            return left_subtree + right_subtree + 1

        min_depth = min(left_subtree, right_subtree)

        return min_depth + 1


class Solution2:
    '''
    2. DFS recursive
    Easy to understand
    '''

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        # If node has one or more None, then we need to handle it.
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1

        left_subtree = self.minDepth(root.left)
        right_subtree = self.minDepth(root.right)

        return min(left_subtree, right_subtree) + 1

# TODO: 3 more solutions!!


class Solution:
    '''
    Leetcode solution
    '''

    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        children = [root.left, root.right]
        # if we're at leaf node
        if root.left is None and root.right is None:
            return 1

        # the node has one or more child nodes.
        min_depth = float('inf')
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)

        return min_depth + 1


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
