# Author: leetcode + kei
# Date: May 31, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest

import collections


class Solution:
    def __init__(self):
        pass

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def traverse(node):
            if node is None:
                return 'N'
            # Do preorder serialization.
            # We can use any order traversal as long as we use null.
            serialized = "{},{},{}".format(
                str(node.val),
                traverse(node.left),
                traverse(node.right))
            # Put the root of this subtree with the serialized structure being as a key.
            grouped_subtrees[serialized].append(node)
            return serialized

        # To group duplicate subtrees, serialize all the subtrees including null.
        # Using dict, find duplicates.
        # K: serialized subtree (structure of subtree), V: root of subtree
        grouped_subtrees = collections.defaultdict(list)
        traverse(root)
        # Pick up only duplicates.
        root_nodes = [grouped_subtrees[serialized][0]
                      for serialized in grouped_subtrees
                      if len(grouped_subtrees[serialized]) >= 2]
        return root_nodes


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
