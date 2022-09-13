# Author: leetcode + kei
# Date: September 13, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    The input of the recursion stack is a root node of BST.
    The output of the recursion stack is the root nodes of left subtree and right
    subtree.

    Return subtrees array, where
    ret[0] is always a root node of the subtree that has all the nodes
    smaller than or equal to target.
    ret[1] is always a root node of the subtree that has all the nodes
    bigger than target.

    O(H) time and space, where H is the height of the input tree.
    '''

    def __init__(self):
        pass

    def splitBST(self,
                 root: Optional[TreeNode],
                 target: int) -> List[Optional[TreeNode]]:

        def dfs(node: TreeNode, target: int) -> List[TreeNode]:
            if node is None:
                return [None, None]

            ret = [None, None]
            # By comparing the target with the current node value,
            # we know we should go which way. Think twice about the condition!
            # Since target value node must be in left subtree,
            # do not include '=' in the if condition.
            if target < node.val:
                # Go left.
                # It is confirmed that the current node is a root of the right subtree.
                # Note that the left child of the current node will be determined by
                # the recursive function.
                subtrees = dfs(node.left, target)
                node.left = subtrees[1]
                ret[1] = node
                # The root of left subtree will be determined by the recursive function.
                ret[0] = subtrees[0]
            else:
                # Go right.
                subtrees = dfs(node.right, target)
                node.right = subtrees[0]
                ret[0] = node
                ret[1] = subtrees[1]

            return ret

        return dfs(root, target)


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_output = [
            # (input1, input2, expected output) depending on number of arguments
            ([0, 1, 2], 3, 6),
            ([0, 1], 3, 5),
        ]
        s = Solution()
        for case, (input1, input2, expected) in enumerate(
                input_and_expected_output):
            print('Case: {}'.format(case))
            with self.subTest(input1=input1, input2=input2, expected=expected):
                result = s.topKFrequent(input1, input2)
                self.assertEqual(result, expected)

    # def test_tree(self):
    #     '''
    #     Tree test example
    #     '''
    #     # Binary Tree
    #     #     6
    #     #    /  \
    #     #   3    12
    #     #  / \   / \
    #     # 1   4 9  14

    #     n1 = TreeNode(6)
    #     n2 = TreeNode(3)
    #     n3 = TreeNode(12)
    #     n4 = TreeNode(1)
    #     n5 = TreeNode(4)
    #     n6 = TreeNode(9)
    #     n7 = TreeNode(14)

    #     n1.left = n2
    #     n1.right = n3
    #     n2.left = n4
    #     n2.right = n5
    #     n3.left = n6
    #     n3.right = n7

    #     s = Solution()
    #     input_and_expected_outputs = [
    #         # (input1, input2, expected output) depending on number of arguments
    #         (n1, n6, n7, n3),
    #         (n1, n3, n5, n1),
    #         (n1, n4, n5, n1),  # Fail
    #     ]
    #     s = Solution()
    #     for input1, input2, input3, expected in input_and_expected_outputs:
    #         with self.subTest(input1=input1.val, input2=input2.val, input3=input3.val,
    #                           expected=expected.val):
    #             result = s.solve(input1, input2, input3)
    #             self.assertEqual(result, expected)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
