# Author: girikuncoro + kei
# Date: July 24, 2021
from typing import *
from helper_classes import *


class Solution:

    D = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    count += 1
        return count

    def dfs(self, grid, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or \
                grid[r][c] != '1':
            return

        grid[r][c] = '#'
        for d in self.D:
            self.dfs(grid, r+d[0], c+d[1])


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 8
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
