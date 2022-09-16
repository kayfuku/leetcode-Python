# Author: girikuncoro + kei
# Date: July 24, 2021, September 14, 2022
from logging.handlers import QueueListener
import unittest
from typing import *
from helper_classes import *
from collections import *


class Solution:
    '''
    1. DFS
    O(MN) time and space, where M is the number of rows and N is the number of coloumns.
    '''

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or \
                    grid[r][c] == WATER or grid[r][c] == VISITED:
                return

            grid[r][c] = VISITED
            for d in D:
                dfs(r + d[0], c + d[1])

        count = 0
        # [up, right, down, left]
        D = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        WATER = '0'
        ISLAND = '1'
        VISITED = '2'
        R = len(grid)
        C = len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == ISLAND:
                    dfs(r, c)
                    count += 1

        return count


class Solution2:
    '''
    2. BFS
    O(MN) time, O(M + N) space
    '''

    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(r, c):
            q = deque()
            q.append([r, c])
            grid[r][c] = VISITED
            while q:
                size = len(q)
                for i in range(size):
                    r, c = q.popleft()
                    for d in D:
                        nr = r + d[0]
                        nc = c + d[1]
                        if nr < 0 or nr >= R or nc < 0 or nc >= C or \
                                grid[nr][nc] == WATER or grid[nr][nc] == VISITED:
                            continue
                        q.append([nr, nc])
                        grid[nr][nc] = VISITED

        if not grid:
            return 0

        D = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        WATER = '0'
        ISLAND = '1'
        VISITED = '2'
        R = len(grid)
        C = len(grid[0])
        count = 0
        for row in range(R):
            for col in range(C):
                if grid[row][col] == ISLAND:
                    bfs(row, col)
                    count += 1

        return count


class Solution3:
    '''
    3. Union Find
    '''

    def numIslands(self, grid: List[List[str]]) -> int:

        return 0


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
