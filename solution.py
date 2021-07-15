# Author: + kei
# Date: July ?, 2021
from typing import *


class Solution:
    def solve(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, v in enumerate(nums):
            print(i, v)

        return nums


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 8
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
