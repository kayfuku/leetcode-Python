# Author: leetcode + kei
# Date: May 15, 2022
from typing import *
from helper_classes import *
import numpy as np


class Solution:
    def __init__(self):
        pass

    # The isBadVersion API is already defined for you.
    def isBadVersion(self, version: int) -> bool:
        pass

    def firstBadVersion(self, n: int) -> int:
        '''
        Binary Search to find leftmost x
        '''
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            ret = self.isBadVersion(mid)
            if ret:
                right = mid - 1
            else:
                left = mid + 1
        return left


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 2
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
