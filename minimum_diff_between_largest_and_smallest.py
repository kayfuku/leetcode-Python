# Author: lee215 + kei
# Date: September 15, 2021
from typing import *
from helper_classes import *
import numpy as np


class Solution:
    def minDifference(self, A: List[int]) -> int:
        A.sort()
        return min(b - a for a, b in zip(A[:4], A[-4:]))


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 2
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
