# Author: leetcode + kei
# Date: August 21, 2022
from re import S
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest

from collections import defaultdict


class Solution:
    '''
    NG! Review again!
    '''

    def __init__(self, dictionary: List[str]):
        # K: abbr, V: set of words whose abbriviation is that key.
        self.dic = defaultdict(set)
        for word in dictionary:
            abbr = self.to_abbr(word)
            self.dic[abbr].add(word)

    def to_abbr(self, word: str) -> str:
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]

    def isUnique(self, word: str) -> bool:
        # 'word' might not be in the original dictionary.
        abbr = self.to_abbr(word)
        # Caution! Unlike java, this puts abbr in the dic, which doesn't work in the next line.
        # set_words = self.dic[abbr]
        # return abbr not in self.dic or (len(set_words) == 1 and word in set_words)
        if abbr not in self.dic:
            return True
        set_words = self.dic[abbr]
        return len(set_words) == 1 and word in set_words


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_outputs = [
            # (input1, input2, expected output) depending on number of arguments
            # ("dear", False),
            ("cart", True),
            # ("cane", False),
            # ("make", True),
            # ("cake", True),
        ]
        s = Solution(["deer", "door", "cake", "card"])
        for input1, expected in input_and_expected_outputs:
            with self.subTest(input1=input1, expected=expected):
                result = s.isUnique(input1)
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
