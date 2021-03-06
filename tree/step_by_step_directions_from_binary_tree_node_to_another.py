# Author: leetcode + kei
# Date: May 8, 2022
import unittest
from typing import *
from helper_classes import *
import numpy as np


class Solution:

    def __init__(self):
        pass

    def lowest_common_ancestor(
            self, root: TreeNode, p: int, q: int) -> TreeNode:
        def recurse_tree(curr_node):
            if not curr_node or curr_node.val == p or curr_node.val == q:
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

    def getDirections(
            self, root: Optional[TreeNode],
            start_value: int, dest_value: int) -> str:
        ancestor = self.lowest_common_ancestor(root, start_value, dest_value)

        def get_direction(node: TreeNode, value: int, steps: List[str]):
            if not node:
                return False
            if node.val == value:
                return True
            steps.append('L')
            if get_direction(node.left, value, steps):
                return True
            steps.pop()
            steps.append('R')
            if get_direction(node.right, value, steps):
                return True
            steps.pop()
            return False

        to_start = []
        get_direction(ancestor, start_value, to_start)
        to_dest = []
        get_direction(ancestor, dest_value, to_dest)

        direction = []
        for _ in range(len(to_start)):
            direction.append('U')
        for d in to_dest:
            direction.append(d)

        return ''.join(direction)


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
