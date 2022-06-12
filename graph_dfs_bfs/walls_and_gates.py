# Author: leetcode + kei
# Date: June 11, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest

from collections import deque


class Solution:
    '''
    BFS
    '''

    def __init__(self):
        pass

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        GATE = 0
        # down, up, left, right
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        if rooms is None:
            return []
        # Initialize the queue with all 0s.
        R, C = len(rooms), len(rooms[0])
        # Instead of doing BFS from each square, we do BFS from each gate.
        # Put all the gates first so that we do BFS one at a time for each gate.
        q = deque()
        for r in range(R):
            for c in range(C):
                if rooms[r][c] == GATE:
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in DIR:
                nr = r + dr
                nc = c + dc
                # rooms[nr][nc] > rooms[r][c] means that,
                # next square is empty or the other gate is farther than this gate.
                if 0 <= nr < R and 0 <= nc < C and rooms[nr][nc] > rooms[r][c]:
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))


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
