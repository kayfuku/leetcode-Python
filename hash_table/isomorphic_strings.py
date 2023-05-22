# Author: leetcode + kei
# Date: May 24, 2022
import re
from typing import *
from helper_classes import *
import numpy as np
import unittest


class Solution:
    def __init__(self):
        pass

    def isIsomorphic(self, s, t):
        s_to_t = {}
        t_to_s = {}

        for c1, c2 in zip(s, t):
            # First, check if the character is already mapped
            # because the code will be simpler.
            if (c1 not in s_to_t) and (c2 not in t_to_s):
                s_to_t[c1] = c2
                t_to_s[c2] = c1
            elif s_to_t.get(c1) != c2 or t_to_s.get(c2) != c1:
                return False

        return True

    def isIsomorphic2(self, s: str, t: str) -> bool:
        '''
           01234
        s: paper
        t: title
        The last index of the character is the same.
        '''
        # K: character, V: index
        map_s_idx = {}
        map_t_idx = {}
        for i, (c1, c2) in enumerate(zip(s, t)):
            # Use get(key, default) instead of map[key] to avoid KeyError.
            # Use -1 as default value because index starts from 0.
            if map_s_idx.get(c1, -1) != map_t_idx.get(c2, -1):
                return False
            map_s_idx[c1] = i
            map_t_idx[c2] = i

        return True


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
