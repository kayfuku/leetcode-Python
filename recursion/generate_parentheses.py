# Author: leetcode + kei
# Date: October 16, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class temp_listolution:
    '''
    Recursion
    to choose one from two items.
    We need '(' before adding ')'. We can use the number of those parentheses to
    check if we can add them.
    '''

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(temp_list=[], left=0, right=0):
            if len(temp_list) == n * 2:
                ans.append(''.join(temp_list))
                return

            # We can add '(' until the number of it reaches n.
            if left < n:
                # Go to left branch.
                # (Partial candidate solution)
                temp_list.append('(')
                # (Explore further)
                backtrack(temp_list, left + 1, right)
                # (Backtracking)
                temp_list.pop()

            # We can add ')' if the number of ')' is less than '('.
            if right < left:
                # Go to right branch.
                temp_list.append(')')
                backtrack(temp_list, left, right + 1)
                temp_list.pop()

        backtrack()
        return ans


class Testtemp_listolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_output = [
            # (input1, input2, expected output) depending on number of arguments
            ([0, 1, 2], 3, 6),
            ([0, 1], 3, 5),
        ]
        s = temp_listolution()
        for case, (input1, input2, expected) in enumerate(
                input_and_expected_output):
            print('Case: {}'.format(case))
            with self.subTest(input1=input1, input2=input2, expected=expected):
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

    #     s = temp_listolution()
    #     input_and_expected_outputs = [
    #         # (input1, input2, expected output) depending on number of arguments
    #         (n1, n6, n7, n3),
    #         (n1, n3, n5, n1),
    #         (n1, n4, n5, n1),  # Fail
    #     ]
    #     s = temp_listolution()
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
