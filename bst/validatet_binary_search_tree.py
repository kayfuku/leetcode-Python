# Author: leetcode + kei
# Date: July 21, 2021, September 12, 2022
import unittest
from typing import *
from helper_classes import *


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:

        def validate(node, low=None, high=None):
            # Empty trees are valid BSTs.
            if node is None:
                return True
            # The current node's value must be between low and high.
            if low is not None and node.val <= low:
                return False
            if high is not None and node.val >= high:
                return False

            # The left and right subtree must also be valid.
            return validate(node.left, low, node.val) and \
                validate(node.right, node.val, high)

        return validate(root)


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
