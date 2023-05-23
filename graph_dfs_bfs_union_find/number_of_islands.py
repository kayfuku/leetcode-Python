# Author: girikuncoro + kei
# Date: July 24, 2021, September 14, 2022, May 23, 2023
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
            if r < 0 or r >= self.R or c < 0 or c >= self.C or \
                    grid[r][c] == self.WATER or grid[r][c] == self.VISITED:
                return

            grid[r][c] = self.VISITED
            for d in self.D:
                dfs(r + d[0], c + d[1])

        count = 0
        # [up, right, down, left]
        self.D = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        self.WATER = '0'
        self.ISLAND = '1'
        self.VISITED = '2'
        self.R = len(grid)
        self.C = len(grid[0])
        for row in range(self.R):
            for col in range(self.C):
                if grid[row][col] == self.ISLAND:
                    dfs(row, col)
                    count += 1

        return count


class Solution2:
    '''
    2. BFS
    O(MN) time, O(M + N) space
    '''

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def bfs(r, c):
            q = deque()
            # Adding to the queue and marking as visited.
            q.append((r, c))
            grid[r][c] = self.VISITED
            while q:
                size = len(q)
                for i in range(size):
                    r, c = q.popleft()
                    # Neighbors
                    for d in self.D:
                        nr = r + d[0]
                        nc = c + d[1]
                        if nr < 0 or nr >= self.R or nc < 0 or nc >= self.C or \
                                grid[nr][nc] == self.WATER or grid[nr][nc] == self.VISITED:
                            continue
                        # Adding and marking as visited must be at the same time!
                        # because two children can have the same child node.
                        q.append((nr, nc))
                        grid[nr][nc] = self.VISITED

        self.D = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.WATER = '0'
        self.ISLAND = '1'
        self.VISITED = '2'
        self.R = len(grid)
        self.C = len(grid[0])
        count = 0
        for row in range(self.R):
            for col in range(self.C):
                if grid[row][col] == self.ISLAND:
                    bfs(row, col)
                    count += 1

        return count


class Solution3:
    '''
    3. Union Find

    ex)
    2 - 0 - 3                2 - 0 - 3
                 ==========> |
    1 - 4                    1 - 4
    i: 0 1 2 3 4 unite(4, 0) i: 0 1 2 3 4
    p: 2 1 2 0 1 ==========> p: 2 2 2 0 2
    '''

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        R = len(grid)
        C = len(grid[0])
        self.count = sum(grid[r][c] == '1' for r in range(R) for c in range(C))
        # Initialization. Every node has its own node as a parent node (each node is isolated).
        # Assign node index and store the coordinate of itself as the parent coordinate.
        parent = [i for i in range(R * C)]

        def find(x):
            '''
            Return root of the graph that contains x.
            '''
            if parent[x] == x:
                return parent[x]
            return find(parent[x])

        def unite(x, y):
            xroot = find(x)
            yroot = find(y)
            if xroot == yroot:
                # x and y are already in the same graph.
                return
            # The roots of two graphs are different.
            # Connecting them together, the parent of x will be yroot.
            parent[xroot] = yroot
            self.count -= 1

        WATER = '0'
        for r in range(R):
            for c in range(C):
                if grid[r][c] == WATER:
                    continue
                index = r * C + c
                # Unite '1' and the right or down neighbor '1'.
                if c + 1 < C and grid[r][c + 1] == '1':
                    unite(index, index + 1)
                if r + 1 < R and grid[r + 1][c] == '1':
                    unite(index, index + C)

        return self.count


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
