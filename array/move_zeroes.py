# Author: OldCodingFarmer + kei
# Date: August 10, 2021
from typing import *
from helper_classes import *
import numpy as np


class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                # swap
                nums[i], nums[p] = nums[p], nums[i]
                p += 1


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 2
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
