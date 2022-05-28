# Author: leetcode + kei
# Date: May 25, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest


class Solution:
    '''
    Use dict to count
    '''

    def __init__(self):
        pass

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = {}
        for num in nums1:
            counts[num] = counts.get(num, 0) + 1
        # counts = collections.Counter(nums1)

        res = []
        for num in nums2:
            if num in counts and counts[num] > 0:
                res.append(num)
                counts[num] -= 1

        return res


class Solution2:
    '''
    Two pointers
    If the arrays are sorted (or the output needs to be sorted), this could
        be the first solution.
    '''

    def __init__(self):
        pass

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        p1 = p2 = 0
        res = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1

        return res


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        For more than one argument
        For one argument, comment out some lines.
        '''
        input_and_expected_outputs = [
            # ((input), expected output) or
            # (input, expected output) depending on number of arguments
            (([0, 1, 2], 3), 6),
            (([0, 1], 3), 5),
        ]
        s = Solution()
        for input, expected in input_and_expected_outputs:
            # result = s.solve(input)
            result = s.solve(*input)
            self.assertEqual(result, expected)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
