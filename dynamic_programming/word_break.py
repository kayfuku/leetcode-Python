# Author: leetcode + kei
# Date: October 22, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    DP
    O(n^3) time, O(n) space
    (slicing takes O(n) time)
    '''

    def wordBreak(self, S: str, word_dict: List[str]) -> bool:
        word_set = set(word_dict)
        n = len(S)
        dp = [False] * (n + 1)
        # dp: True if all chars to the left of the current index can meet the requirement.
        dp[0] = True

        # Check every substring S[s:e] in the S and keep the result to the left of it.
        # Note that end index is outer loop starting from 1. If the end index is inner loop,
        # it would overwrite dp.
        for e in range(1, n + 1):
            for s in range(e):
                # Check if the substring is in the dictionary and the result to
                # the left of it is True, which means it can be split into substrings
                # in the dictionary so far.
                if S[s:e] in word_set and dp[s]:
                    # Save the result at index e so that we don't have to check
                    # this char and chars before it again.
                    dp[e] = True
                    break

        return dp[n]


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_output = [
            # (input1, input2, expected output) depending on number of arguments
            ("leetcode", ["leet", "code"], True),
        ]
        s = Solution()
        for case, (input1, input2, expected) in enumerate(
                input_and_expected_output):
            print('Case: {}'.format(case))
            with self.subTest(input1=input1, input2=input2, expected=expected):
                result = s.wordBreak(input1, input2)
                self.assertEqual(result, expected)

    # def test_tree(self):
    #     '''
    #     Tree test example
    #     '''
    #     # Binary Tree
    #     #     6
    #     #    /  \
    #     #   3    12
    #     #  / \   / \
    #     # 1   4 9  14

    #     n1 = TreeNode(6)
    #     n2 = TreeNode(3)
    #     n3 = TreeNode(12)
    #     n4 = TreeNode(1)
    #     n5 = TreeNode(4)
    #     n6 = TreeNode(9)
    #     n7 = TreeNode(14)

    #     n1.left = n2
    #     n1.right = n3
    #     n2.left = n4
    #     n2.right = n5
    #     n3.left = n6
    #     n3.right = n7

    #     s = Solution()
    #     input_and_expected_outputs = [
    #         # (input1, input2, expected output) depending on number of arguments
    #         (n1, n6, n7, n3),
    #         (n1, n3, n5, n1),
    #         (n1, n4, n5, n1),  # Fail
    #     ]
    #     s = Solution()
    #     for input1, input2, input3, expected in input_and_expected_outputs:
    #         with self.subTest(input1=input1.val, input2=input2.val, input3=input3.val,
    #                           expected=expected.val):
    #             result = s.solve(input1, input2, input3)
    #             self.assertEqual(result, expected)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
