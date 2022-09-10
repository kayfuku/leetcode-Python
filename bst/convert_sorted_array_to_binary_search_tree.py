# Author: leetcode + kei
# Date: July 21, 2021, September 10, 2022
from tkinter.tix import Tree
import unittest
from typing import *
from helper_classes import *


class Solution:
    '''
    We can use preorder traversal to create BST from array.
    First, we have to pick a root node. Then, attach children nodes.
    Height-balanced tree can be created by choosing a middle element in the array
    because the elements to the left of the middle element will be in the left
    subtree and the elements to the right of the middle element will be in the
    right subtree.
    O(N) time and space
    '''

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # We can use 'nums' in this inner method without passing it as an argument.
        def helper(left: TreeNode, right: TreeNode) -> TreeNode:
            if left > right:
                return None

            # Height-balanced restriction means that at each step we have to
            # pick up the number in the middle as a root so that the heights of
            # left and right subtrees are almost the same.
            mid = (left + right) // 2

            # Preorder traversal: node -> left -> right
            node = TreeNode(nums[mid])
            node.left = helper(left, mid - 1)
            node.right = helper(mid + 1, right)

            # Return the root node.
            return node

        return helper(0, len(nums) - 1)


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
