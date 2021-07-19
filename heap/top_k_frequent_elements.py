# Author: leetcode + kei
# Date: July 18, 2021
from typing import *
from helper_classes import *
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(1) time
        if k == len(nums):
            return nums

        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)
        # print('count:', count)
        # print('count.keys():', count.keys())
        # print('count.get(1):', count.get(1))

        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(NlogK) time
        return heapq.nlargest(k, count.keys(), key=count.get)


def main():
    """ For testing """
    s = Solution()

    # Test args
    nums = [1, 2, 1, 1, 2, 3]
    target = 2
    print(s.topKFrequent(nums, target))


if __name__ == '__main__':
    main()
