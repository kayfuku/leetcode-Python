# Author: idontknoooo + kei
# Date: May 9, 2022
from typing import *
from helper_classes import *
import numpy as np


class Solution:
    def __init__(self):
        pass

    def removeOnes(self, grid: List[List[int]]) -> bool:
        r1, r1_invert = grid[0], [1-val for val in grid[0]]
        for i in range(1, len(grid)):
            # "Pattern" of each row should be the same.
            if grid[i] != r1 and grid[i] != r1_invert:
                return False
        return True


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 2
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
