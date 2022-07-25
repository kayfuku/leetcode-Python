# Author: leetcode + kei
# Date: July 24, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    Binary Search Tree can be created from a sorted list.
    All the elements to the left of the root element belong to left subtree.
    All the elements to the right of the root element belong to right subtree.
    '''

    def __init__(self):
        pass

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def generate_trees(start, end):
            if start > end:
                return [None, ]

            all_trees = []
            # Iterate through the sorted list, and pick up a root i.
            # The sorted list is from start to end inclusive.
            for i in range(start, end + 1):
                # Get all the structually unique left subtrees from the
                # sorted list to the left of i.
                left_trees = generate_trees(start, i - 1)

                # Get all the structually unique right subtrees from the
                # sorted list to the right of i.
                right_trees = generate_trees(i + 1, end)

                # All the combinations of the left subtrees and the right subtrees.
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        # Connect left and right subtrees to the root i.
                        # Note that left_tree and/or right_tree could be None.
                        current_tree = TreeNode(i)
                        current_tree.left = left_tree
                        current_tree.right = right_tree

                        all_trees.append(current_tree)

            return all_trees

        return generate_trees(1, n)


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
        #     6
        #    /  \
        #   3    12
        #  / \   / \
        # 1   4 9  14

        n1 = TreeNode(6)
        n2 = TreeNode(3)
        n3 = TreeNode(12)
        n4 = TreeNode(1)
        n5 = TreeNode(4)
        n6 = TreeNode(9)
        n7 = TreeNode(14)

        n1.left = n2
        n1.right = n3
        n2.left = n4
        n2.right = n5
        n3.left = n6
        n3.right = n7

        s = Solution()
        input_and_expected_outputs = [
            # (input1, input2, expected output) depending on number of arguments
            (n1, n6, n7, n3),
            (n1, n3, n5, n1),
            (n1, n4, n5, n1),  # Fail
        ]
        s = Solution()
        for input1, input2, input3, expected in input_and_expected_outputs:
            with self.subTest(input1=input1.val, input2=input2.val, input3=input3.val,
                              expected=expected.val):
                result = s.solve(input1, input2, input3)
                self.assertEqual(result, expected)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
