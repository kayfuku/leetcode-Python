# Author: leetcode + kei
# Date: August 10, 2021
from typing import *
from helper_classes import *


class Solution:
    def merge(
            self, nums1: List[int],
            m: int, nums2: List[int],
            n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1

        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                # nums2 finished.
                # The remaining is already filled.
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                # if nums1 finished, then keep copying nums2
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 8
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
