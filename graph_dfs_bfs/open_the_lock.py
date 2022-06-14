# Author: leetcode + kei
# Date: June 12, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest

from collections import deque


class Solution:
    def __init__(self):
        pass

    def openLock(self, deadends: List[str], target: str) -> int:

        def neighbors(node):
            for i in range(4):
                # Choose one digit.
                x = int(node[i])
                for d in (-1, 1):
                    # 0 down => 9, 9 up => 0
                    y = (x + d) % 10
                    # Insert y at i in the node.
                    yield node[:i] + str(y) + node[i + 1:]

        dead = set(deadends)

        # BFS
        # (node, depth), depth will be the minimum number of turns.
        # list is needed when passing initial value.
        queue = deque([('0000', 0)])
        seen = {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth
            if node in dead:
                continue
            for nei in neighbors(node):
                if nei not in seen:
                    queue.append((nei, depth + 1))
                    seen.add(nei)

        return -1


class Solution2:
    '''
    Without generator
    '''

    def __init__(self):
        pass

    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)

        # BFS
        queue = deque()
        # (node, depth), depth will be the minimum number of turns.
        queue.append(('0000', 0))
        visited = set('0000')
        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth
            if node in dead:
                continue
            # Check neighbors.
            for i in range(4):
                # Choose one digit.
                x = int(node[i])
                for d in (-1, 1):
                    # 0 down => 9, 9 up => 0
                    y = (x + d) % 10
                    # Insert y at i in the node.
                    nei = node[:i] + str(y) + node[i + 1:]
                    if nei not in visited:
                        queue.append((nei, depth + 1))
                        visited.add(nei)

        return -1


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_outputs = [
            # (input, input, expected output) depending on number of arguments
            ([0, 1, 2], 3, 6),
            ([0, 1], 3, 5),
        ]
        s = Solution()
        for input1, input2, expected in input_and_expected_outputs:
            with self.subTest(input1=input1, input2=input2):
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
        result = s.countUnivalSubtrees(n1)
        self.assertEqual(result, 4)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
