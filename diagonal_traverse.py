# Author: leetcode + kei
# Date: June 25, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest


class Solution:
    def __init__(self):
        pass

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # Returns [] if matrix is None or an empty list.
        # This does not return True if matrix is [[]], but it's ok.
        # R will be 1, and C will be 0 in that case.
        if matrix is None or len(matrix) == 0:
            return []

        R, C = len(matrix), len(matrix[0])
        result, intermediate = [], []

        # We have to go over all the elements in the first
        # row and the last column to cover all possible diagonals.
        for d in range(R + C - 1):
            intermediate.clear()

            # We need to figure out the "head" of this diagonal.
            # The elements in the first row and the last column
            # are the respective heads.
            r = 0 if d < C else d - C + 1
            c = d if d < C else C - 1

            # TODO:
            # Iterate until one of the indices goes out of scope
            # Take note of the index math to go down the diagonal
            while r < R and c > -1:
                intermediate.append(matrix[r][c])
                r += 1
                c -= 1

            # Reverse even numbered diagonals. The
            # article says we have to reverse odd
            # numbered articles but here, the numbering
            # is starting from 0 :P
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)

        return result


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
