# Author: SimplyFaisal + kei
# Date: August 9, 2021
from typing import *
from helper_classes import *


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""

        for j, ch in enumerate(strs[0]):
            for i, string in enumerate(strs[1:]):
                if len(string) == j or string[j] != ch:
                    return strs[0][:j]

        return strs[0]


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 8
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
