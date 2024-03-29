# Author: leetcode + kei
# Date: July 6, 2022, December 13, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest
from collections import *


class Node:
    def __init__(self, val: int = 0, left: Node = None, right: Node = None,
                 next: Node = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    '''
    BFS (Level order traversal) in a tree.
    '''

    def __init__(self):
        pass

    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root

        # BFS (Level order traversal) from right to left.
        q = deque([root])
        while q:
            size = len(q)
            prev = None
            for i in range(size):
                curr = q.popleft()
                curr.next = prev
                # Right first!
                if curr.right:
                    q.append(curr.right)
                # Then left.
                if curr.left:
                    q.append(curr.left)

                prev = curr

        return root


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

    # def test_tree(self):
    #     '''
    #     Tree test example
    #     '''
    #     n1 = TreeNode(5)
    #     n2 = TreeNode(1)
    #     n3 = TreeNode(5)
    #     n4 = TreeNode(5)
    #     n5 = TreeNode(5)
    #     n6 = TreeNode(5)

    #     n1.left = n2
    #     n1.right = n3
    #     n3.right = n6
    #     n2.left = n4
    #     n2.right = n5

    #     s = Solution()
    #     result = s.solve(n1)
    #     self.assertEqual(result, 4)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
