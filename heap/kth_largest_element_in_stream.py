# Author: cenkay + kei
# Date: July 17, 2021
from typing import *
from helper_classes import *
import heapq


class KthLargest:

    def __init__(self, k, nums):
        self.nums = nums
        self.k = k
        # create min heap
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val):
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        # peek
        return self.nums[0]

    # Your KthLargest object will be instantiated and called as such:
    # obj = KthLargest(k, nums)
    # param_1 = obj.add(val)


def main():
    """ For testing """
    s = KthLargest()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 8
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
