# Author: leetcode + kei
# Date: November 27, 2022
from typing import *
from helper_classes import *
from collections import *
from sortedcontainers import SortedList, SortedSet, SortedDict
import heapq
import numpy as np
import unittest


class Solution:
    '''
    1. Use height without removing leaf nodes
    Good for interview
    It's a little like a level order traversal with recursion.
    Author: kei
    '''

    def findLeaves(self, root: TreeNode) -> List[List[int]]:

        def get_height(node: TreeNode) -> int:
            if not node:
                return -1

            left_height = get_height(node.left)
            right_height = get_height(node.right)
            curr_height = max(left_height, right_height) + 1

            if len(ret) == curr_height:
                ret.append([])
            ret[curr_height].append(node.val)

            return curr_height

        ret = []
        get_height(root)
        return ret


class Solutin2:
    '''
    2. FYI, actually remove leaf nodes
    Author: shawn2010 + kei
    '''

    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        while root:
            curr_leaves = []
            root = self._find_leaves(root, curr_leaves)
            result.append(curr_leaves)

        return result

    def _find_leaves(self, node: TreeNode, curr_leaves: List[int]) -> TreeNode:
        if not node:
            return None
        if not node.left and not node.right:
            # The node is a leaf.
            curr_leaves.append(node.val)
            return None

        node.left = self._find_leaves(node.left, curr_leaves)
        node.right = self._find_leaves(node.right, curr_leaves)

        return node


class Try:
    '''
    TODO:
    '''

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        return 0


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        Change input and expected output as needed.
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
                # Change to the method name to be tested.
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
