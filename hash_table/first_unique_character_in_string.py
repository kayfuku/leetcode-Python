# Author: leetcode + kei
# Date: July ?, 2021
from typing import *
from helper_classes import *
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        O(N) time and space
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)

        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx

        return -1


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 8
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
