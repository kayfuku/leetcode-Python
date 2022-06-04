# Author: leetcode + kei
# Date: June 1, 2022
from turtle import right
from typing import *
from helper_classes import *
import numpy as np
import unittest


class Solution:
    def __init__(self):
        self.count = 0

    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:

        def is_unival_subtree(node):
            if node is None:
                return True

            # We need count, which means we need to traverse all the nodes.
            left_is_uni = is_unival_subtree(node.left)
            right_is_uni = is_unival_subtree(node.right)
            # Note that the below if statement including recursive func is not
            # working because we might not be able to traverse right subtrees.
            # if not is_unival_subtree(node.left) or \
            #         not is_unival_subtree(node.right):
            if not left_is_uni or not right_is_uni:
                return False

            # Be careful about null nodes.
            if (node.left is not None and node.val != node.left.val) or \
                    (node.right is not None and node.val != node.right.val):
                return False

            self.count += 1
            return True

        is_unival_subtree(root)
        return self.count


class Solution2:
    def __init__(self):
        self.count = 0

    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:

        def is_unival_subtree_and_same_val_as_parent(node, parent_val):
            if node is None:
                return True

            # We need count, which means we need to traverse all the nodes.
            left_is_uni = is_unival_subtree_and_same_val_as_parent(
                node.left, node.val)
            right_is_uni = is_unival_subtree_and_same_val_as_parent(
                node.right, node.val)
            # Note that the below if statement including recursive func is not
            # working because we might not be able to traverse right subtrees.
            # if not is_unival_subtree_and_same_val_as_parent(node.left) or \
            #         not is_unival_subtree_and_same_val_as_parent(node.right):
            if not left_is_uni or not right_is_uni:
                return False

            # At this point, this subtree is a univalue subtree.
            self.count += 1

            return node.val == parent_val

        # Any value will be fine in the second arg because it won't affect the count.
        is_unival_subtree_and_same_val_as_parent(root, 0)
        return self.count


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        For more than one argument
        For one argument, comment out some lines.
        '''
        input_and_expected_outputs = [
            # ((input), expected output) or
            # (input, expected output) depending on number of arguments
            (([0, 1, 2], 3), 6),
            (([0, 1], 3), 5),
        ]
        s = Solution()
        for input, expected in input_and_expected_outputs:
            # result = s.solve(input)
            result = s.solve(*input)
            self.assertEqual(result, expected)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
