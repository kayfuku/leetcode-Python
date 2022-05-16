# Author: leetcode + kei
# Date: May 15, 2022
from ast import Num
from typing import *
from helper_classes import *
import numpy as np


class Solution:
    def __init__(self):
        self.pick = 2

    # The guess API is already defined for you.
    # @param num, your guess
    # @return -1 if num is higher than the picked number
    #          1 if num is lower than the picked number
    #          otherwise return 0

    def guess(self, num: int) -> int:
        if num > self.pick:
            return -1
        elif num < self.pick:
            return 1
        else:
            return 0

    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            ret = self.guess(mid)
            if ret == 0:
                return mid
            if ret == -1:
                right = mid - 1
            else:
                left = mid + 1
        return -1


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 2
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
