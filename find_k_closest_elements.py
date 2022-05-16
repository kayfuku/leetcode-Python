# Author: leetcode + kei
# Date: May 15, 2022
from typing import *
from helper_classes import *
import numpy as np


class Solution:
    def __init__(self):
        pass

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        The list we want is [A1, A2, ... x, ... Ak] (len: k).
        Using Binary Search, we're going to find A1.
        Pick up a 'mid' and check if the condition is met.
        'mid' is our attempt to find A1.
        Be careful that x cannot be in the list, and the distance is not defined
        by indices of the list. Also, there can be duplicate numbers in the list.
        ex)
        arr: [0,0,1,2,3,3,4,7,7,8]
        k: 3
        x: 5
        => return [3,3,4]
        We need to keep searching to find leftmost.
        '''
        # Possible bounds of A1
        left = 0
        right = len(arr) - k
        while left <= right:
            mid = (left + right) // 2
            A = x - arr[mid]
            if mid + k == len(arr):
                # Avoid out of bound.
                return arr[mid:]
            B = arr[mid + k] - x
            if A <= B:
                # Search left side.
                right = mid - 1
            else:
                left = mid + 1

        return arr[left:left + k]


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 2
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
