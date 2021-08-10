# Author: leetcode + kei
# Date: July 24, 2021
from typing import *
from helper_classes import *


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        D = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def get_area(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) \
                    or (r, c) in seen or grid[r][c] == 0:
                return 0
            seen.add((r, c))
            area = 1
            for d in D:
                area += get_area(r+d[0], c+d[1])

            return area

        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_area = max(max_area, get_area(r, c))

        return max_area


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 8
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
