# Author: leetcode + kei
# Date: November 6, 2022
from collections import Counter
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    1. Brute Force
    O(N^3) time, O(min(M,N)) space, where N is the string length and M is the
    charset size.
    '''

    def lengthOfLongestSubstring(self, S: str) -> int:

        def check(start, end):
            chars = set()
            for i in range(start, end + 1):
                c = S[i]
                if c in chars:
                    return False

                chars.add(c)

            return True

        n = len(S)
        res = 0
        for s in range(n):
            for e in range(s, n):
                if check(s, e):
                    # e - s + 1 is the substring length.
                    res = max(res, e - s + 1)

        return res


class Solution2:
    '''
    2. Map (Sliding window)
    O(N) time, O(min(M,N)) space
    '''

    def lengthOfLongestSubstring(self, S: str) -> int:
        # count how many for each char
        chars = Counter()
        left = right = 0
        res = 0
        while right < len(S):
            # right char
            rc = S[right]
            chars[rc] += 1

            # Check duplicates.
            while chars[rc] > 1:
                lc = S[left]
                chars[lc] -= 1
                left += 1
            # Assert that the substring 'left' to 'right' does not have dups.

            res = max(res, right - left + 1)
            right += 1

        return res


class Solution3:
    '''
    3. Faster Map (Sliding window)

    '''

    def lengthOfLongestSubstring(self, S: str) -> int:
        n = len(S)
        ans = 0
        # K: substring chars, V: rightmost index of the char
        d = {}

        s = 0
        for e in range(n):
            if S[e] in d:
                # We found this char more than one so far.
                # Keep the start point rightmost index so that the substring
                # does not contain duplicates.
                # Start point moves in O(1) time.
                s = max(d[S[e]], s)

            # e - s + 1 is the substring length.
            ans = max(ans, e - s + 1)
            d[S[e]] = e + 1

        return ans


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        Change input and expected output as needed.
        '''
        input_and_expected_output = [
            # (input1, input2, expected output) depending on number of arguments
            ([0, 1, 2], 3, 6),
            ([0, 1], 3, 5),
        ]
        s = Solution()
        for case, (input1, input2, expected) in enumerate(
                input_and_expected_output):
            print('Case: {}'.format(case))
            with self.subTest(input1=input1, input2=input2, expected=expected):
                # Change to the method name to be tested.
                result = s.topKFrequent(input1, input2)
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
