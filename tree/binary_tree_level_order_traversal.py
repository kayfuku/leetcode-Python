# Author: leetcode + kei
# Date: July 21, 2021, September 11, 2022
from curses import nonl
import unittest
from typing import *
from helper_classes import *

from collections import deque


class Solution:
    '''
    1. BFS
    Good for interview
    '''

    def levelOrder(self, root):
        levels = []
        if not root:
            return levels

        # We don't need this for this problem.
        level = 0

        # BFS
        queue = deque([root, ])
        while queue:
            # start the current level
            list_level = []
            # number of elements in the current level
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                # fulfill the current level
                list_level.append(node.val)

                # add child nodes of the current level
                # in the queue for the next level
                # Left first because problem statement says,
                # "from left to right".
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            levels.append(list_level)

            # go to next level
            level += 1

        return levels


class Solution2:
    '''
    2. DFS, recursive
    Not recommended for interview
    '''

    def levelOrder(self, root):
        levels = []
        if not root:
            return levels

        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels


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
    #     result = s.countUnivalSubtrees(n1)
    #     self.assertEqual(result, 4)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
