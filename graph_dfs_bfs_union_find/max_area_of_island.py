# Author: leetcode + kei
# Date: July 24, 2021, September 17, 2022
import unittest
from typing import *
from helper_classes import *
from collections import *


class Solution:
    '''
    1. DFS recursive
    '''

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        D = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        R = len(grid)
        C = len(grid[0])

        def get_area(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or \
                    grid[r][c] == VISITED or grid[r][c] == WATER:
                return 0

            area = 1
            grid[r][c] = VISITED
            for d in D:
                area += get_area(r + d[0], c + d[1])

            return area

        max_area = 0
        WATER = 0
        ISLAND = 1
        VISITED = 2
        for r in range(R):
            for c in range(C):
                if grid[r][c] == ISLAND:
                    max_area = max(max_area, get_area(r, c))

        return max_area


class Solution2:
    '''
    2. BFS
    '''

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        VISITED = 0

        def bfs(r, c):
            q = deque([(r, c)])
            # Add it to the visited right after adding it to the queue.
            grid[r][c] = VISITED
            cnt = 0
            while q:
                cr, cc = q.popleft()
                cnt += 1
                for d in DIR:
                    nr = cr + d[0]
                    nc = cc + d[1]
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1 and \
                            grid[nr][nc] != VISITED:
                        q.append((nr, nc))
                        # Add it to the visited right after adding it to the queue.
                        grid[nr][nc] = VISITED

            return cnt

        R = len(grid)
        C = len(grid[0])
        max_area = 0
        for row in range(R):
            for col in range(C):
                if grid[row][col] == 1:
                    area = bfs(row, col)
                    max_area = max(max_area, area)

        return max_area

    def maxAreaOfIsland_TLE(self, grid: List[List[int]]) -> int:
        '''
        TLE because we start checking on the same island over and over again.
        '''
        DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def bfs(r, c):
            q = deque([(r, c)])
            seen = set([(r, c)])
            cnt = 0
            while q:
                cr, cc = q.popleft()
                cnt += 1
                for d in DIR:
                    nr = cr + d[0]
                    nc = cc + d[1]
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1 and \
                            (nr, nc) not in seen:
                        q.append((nr, nc))
                        seen.add((nr, nc))

            return cnt

        R = len(grid)
        C = len(grid[0])
        max_area = 0
        for row in range(R):
            for col in range(C):
                if grid[row][col] == 1:
                    area = bfs(row, col)
                    max_area = max(max_area, area)

        return max_area

    def maxAreaOfIsland_WA(self, grid: List[List[int]]) -> int:
        '''
        WA because this is a bad pattern of code for BFS. This does not work when
        there is a cycle in the graph. We must add node to the visited right after adding queue.
        '''
        DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        VISITED = 0

        def bfs(r, c):
            q = deque([(r, c)])
            cnt = 0
            while q:
                cr, cc = q.popleft()
                cnt += 1
                grid[cr][cc] = VISITED
                for d in DIR:
                    nr = cr + d[0]
                    nc = cc + d[1]
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1 and \
                            grid[nr][nc] != VISITED:
                        q.append((nr, nc))

            return cnt

        R = len(grid)
        C = len(grid[0])
        max_area = 0
        for row in range(R):
            for col in range(C):
                if grid[row][col] == 1:
                    area = bfs(row, col)
                    max_area = max(max_area, area)

        return max_area


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_outputs = [
            # (input1, input2, expected output) depending on number of arguments
            # ([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            #   [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            #   [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            #   [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            #   [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            #   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            #   [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            #   [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]], 6),
            ([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [
             0, 0, 0, 1, 1], [0, 0, 0, 1, 1]], 4),
        ]
        s = Solution2()
        for input1, expected in input_and_expected_outputs:
            with self.subTest(input1=input1, expected=expected):
                result = s.maxAreaOfIsland(input1)
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
