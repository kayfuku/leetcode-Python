# Author: vijayzuzu + kei
# Date: July 21, 2021, September 6, 2022
import unittest
from typing import *
from helper_classes import *


class Solution:
    '''
    cum_sum A - cum_sum B = sum of subarray
    '''

    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cum_sum = 0
        # K: cum_sum, V: occurances of cum_sums
        d = dict()
        # Don't forget this!
        # Cumulative sum 0 is needed if the subarray starts from the beginning.
        d[0] = 1
        for i in range(len(nums)):
            # Cumulative sum so far
            cum_sum += nums[i]
            # If the subarray whose sum is cum_sum - k exists, then
            # the subarray whose sum is k exists.
            count += d.get(cum_sum - k, 0)
            # Count the number of specific sums.
            # Since nums[i] can be negative, same cum_sum can show up multiple times.
            d[cum_sum] = d.get(cum_sum, 0) + 1

        return count


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_outputs = [
            # (input1, input2, expected output) depending on number of arguments
            ([5, 6, 7], 1, 0),
        ]
        s = Solution()
        for input1, input2, expected in input_and_expected_outputs:
            with self.subTest(input1=input1, k=input2, expected=expected):
                result = s.subarraySum(input1, input2)
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
