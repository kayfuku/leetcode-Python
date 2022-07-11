# Author: leetcode + kei
# Date: July 8, 2022
from msilib import sequence
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    '''

    def serialize(self, root):
        """
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node, string):
            if node is None:
                # We need None to correctly serialize the structure of a tree.
                # Put comma in to split it when deserializing.
                string += 'None,'
                return string

            # Pre-order traversal.
            string += str(node.val) + ','
            string = dfs(node.left, string)
            string = dfs(node.right, string)
            return string

        return dfs(root, '')

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def dfs(s):
            # Check from the leftmost.
            if s[0] == 'None':
                s.pop(0)
                return None

            # Pre-order traversal.
            node = TreeNode(s[0])
            # Remove the first one.
            s.pop(0)
            node.left = dfs(s)
            node.right = dfs(s)
            return node

        sequence = data.split(',')
        root = dfs(sequence)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


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
