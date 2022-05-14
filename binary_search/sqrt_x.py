# Author: leetcode + kei
# Date: May 14, 2022
from turtle import right
from typing import *
from helper_classes import *
import numpy as np


class Solution:
    def __init__(self):
        pass

    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        # Binary Search
        # sqrt should be in between 1 and x.
        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2
            squared = self.mono(mid)
            if squared == x:
                return mid
            if squared > x:
                right = mid - 1
            else:
                left = mid + 1
        # Why is this?
        return right

    def mono(self, a):
        # This must be monotonically increasing/decreasing function.
        return a * a


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 2
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
