# Author: leetcode + kei
# Date: July 21, 2021, September 11, 2022
import unittest
from typing import *
from helper_classes import *

from collections import deque


class Solution:
    '''
    BFS (Level order traversal)
    Use append() and appendleft() on another deque for return
    '''

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = []
        if root is None:
            return []
        # start with the level 0 with a delimiter
        queue = deque([root, ])
        level = 0

        while queue:
            level_list = deque()
            size = len(queue)
            for i in range(size):
                curr_node = queue.popleft()
                if level % 2 == 0:
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            # we finish one level
            ret.append(level_list)
            level += 1

        return ret


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
