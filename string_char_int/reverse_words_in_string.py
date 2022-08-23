# Author: leetcode + kei
# Date: August 22, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    1. Built-in
    O(N) time and space
    '''

    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


class Solution2:
    '''
    2. Reverse the whole string and then reverse each word
    O(N) time and space
    '''

    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == ' ':
            left += 1

        # remove trailing spaces
        while left <= right and s[right] == ' ':
            right -= 1

        # reduce multiple spaces to single one
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                # s[left] is a space and previous char is not a space.
                output.append(s[left])
            left += 1

        return output

    def reverse(self, char_arr: list, left: int, right: int) -> None:
        while left < right:
            # Swap.
            char_arr[left], char_arr[right] = char_arr[right], char_arr[left]
            left += 1
            right -= 1

    def reverse_each_word(self, char_arr: list) -> None:
        n = len(char_arr)
        start = end = 0

        while start < n:
            # go to the end of the word
            while end < n and char_arr[end] != ' ':
                end += 1
            # reverse the word
            self.reverse(char_arr, start, end - 1)
            # move to the next word
            start = end + 1
            end = start

    def reverseWords(self, s: str) -> str:
        # converst string to char array
        # and trim spaces at the same time
        char_arr = self.trim_spaces(s)

        # reverse the whole string
        self.reverse(char_arr, 0, len(char_arr) - 1)

        # reverse each word
        self.reverse_each_word(char_arr)

        return ''.join(char_arr)


class Solution3:
    '''
    3. Deque of words
    '''

    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == ' ':
            left += 1

        # remove trailing spaces
        while left <= right and s[right] == ' ':
            right -= 1

        d, word = deque(), []
        # push word by word in front of deque
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.appendleft(''.join(word))

        return ' '.join(d)


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_outputs = [
            # (input1, input2, expected output) depending on number of arguments
            ([0, 1, 2], 3, 6),
            ([0, 1], 3, 5),
        ]
        s = Solution()
        for input1, input2, expected in input_and_expected_outputs:
            with self.subTest(input1=input1, input2=input2, expected=expected):
                result = s.solve(input1, input2)
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
