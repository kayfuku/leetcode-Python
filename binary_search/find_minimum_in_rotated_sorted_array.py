# Author: leetcode + kei
# Date: September 19, 2021
from typing import *
from helper_classes import *
import numpy as np


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        # if the last element is greater than the first element then there is no rotation.
        # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
        # Hence the smallest element is first element. A[0]
        if nums[0] < nums[right]:
            return nums[0]

        # Binary search way
        while left <= right:
            # Find the mid element
            mid = left + (right - left) // 2

            if mid != 0 and nums[mid - 1] > nums[mid] or \
               mid == 0 and nums[mid] < nums[mid + 1]:
                return nums[mid]

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1

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
