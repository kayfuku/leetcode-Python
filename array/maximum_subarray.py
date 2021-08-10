# Author: leetcode + kei
# Date: August ?, 2021
from typing import *
from helper_classes import *


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize our variables using the first element.
        curr_sum = max_sum = nums[0]

        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If curr_sum is negative, throw it away. Otherwise, keep adding to it.
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 8
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
