# Author: leetcode + kei
# Date: July 26, 2022
from itertools import count
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    The 'count' sits on each recursion stack.
    We can only place one queen for each row. So, recurse on the rows and
    for each row, iterate through the columns.
    '''

    def __init__(self):
        pass

    def totalNQueens(self, n: int) -> int:

        def backtrack(row, occupied_cols, occupied_diag1, occupied_diag2):
            # Base case
            if row == n:
                # N queens have been placed.
                return 1

            count = 0
            for col in range(n):
                # All the squares have diag1 and diag2 values.
                # All the squares of the diagonal 1 of the (row, col) have the diag1 value.
                diag1 = row - col
                # All the squares of the diagonal 2 of the (row, col) have the diag2 value.
                diag2 = row + col

                # Check if (row, col) is under attack. (Constraints)
                if (col in occupied_cols
                    or diag1 in occupied_diag1
                        or diag2 in occupied_diag2):
                    # It's under attack, then move to the next square.
                    continue

                # We can now place a queen here. (Partial candidate solution)
                occupied_cols.add(col)
                occupied_diag1.add(diag1)
                occupied_diag2.add(diag2)

                # Move on to the next row and get the count. (Explore further)
                count += backtrack(row + 1, occupied_cols, occupied_diag1,
                                   occupied_diag2)

                # We got the count. We're done.
                # Move the queen to the next square to the right. (Backtrack)
                occupied_cols.remove(col)
                occupied_diag1.remove(diag1)
                occupied_diag2.remove(diag2)

            # Return the number of solutions when a queen placed at (row, col) and
            # all the possible cases below this row.
            return count

        # Start with row 0.
        return backtrack(0, set(), set(), set())


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
