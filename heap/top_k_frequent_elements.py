# Author: leetcode + kei
# Date: July 18, 2021, September 3, 2022
import unittest
from typing import *
from helper_classes import *
import heapq


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(1) time
        if k == len(nums):
            print("k is the length of nums.")
            return nums

        # 1. Build a count dictionary.
        # K: number, V: count
        # O(N) time
        count = Counter(nums)
        print('count:', count)
        print('count.keys():', count.keys())
        print('count.get(1):', count.get(1))

        # heapq.nlargest(n, iterable, key function) returns n largests.
        # 'key' function takes as input each element and return something which
        # the sorting is based on.
        # O(NlogK) time
        largests = heapq.nlargest(k, count.keys(), key=count.get)
        return largests


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_output = [
            # (input1, input2, expected output) depending on number of arguments
            ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
            ([1], 1, [1]),
        ]
        s = Solution()
        for case, (input1, input2, expected) in enumerate(
                input_and_expected_output):
            print('Case: {}'.format(case))
            with self.subTest(nums=input1, k=input2, expected=expected):
                result = s.topKFrequent(input1, input2)
                self.assertEqual(result, expected)

    # def test_tree(self):
    #     '''
    #     Tree test example
    #     '''
    #     n1 = TreeNode(5)
    #     n2 = TreeNode(1)
    #     n3 = TreeNode(5)
    #     n4 = TreeNode(5)
    #     n5 = TreeNode(5)
    #     n6 = TreeNode(5)

    #     n1.left = n2
    #     n1.right = n3
    #     n3.right = n6
    #     n2.left = n4
    #     n2.right = n5

    #     s = Solution()
    #     result = s.countUnivalSubtrees(n1)
    #     self.assertEqual(result, 4)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
