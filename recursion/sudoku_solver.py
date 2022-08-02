# Author: leetcode + kei
# Date: July 30, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    The next solution is better for interview
    '''

    def __init__(self):
        pass

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def could_place(d, row, col):
            """
            Check if one could place a number d in (row, col) cell
            """
            return not (d in rows[row] or d in columns[col] or
                        d in boxes[box_index(row, col)])

        def place_number(d, row, col):
            """
            Place a number d in (row, col) cell
            """
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)

        def remove_number(d, row, col):
            """
            Remove a number which didn't lead
            to a solution
            """
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'

        def move_to_next_cell_and_explore(row, col):
            """
            Call backtrack function in recursion
            to continue to place numbers
            till the moment we have a solution
            """
            if col == N - 1 and row == N - 1:
                # We're in the last cell, that means we have the solution.
                # Unlike Java, this is needed.
                # 'nonlocal' references to the variable in one outer scope.
                nonlocal sudoku_solved
                sudoku_solved = True
            elif col == N - 1:
                # We're in the end of the row.
                # Go to the first column of the next row.
                backtrack(row + 1, 0)
            else:
                # Go to the next column.
                backtrack(row, col + 1)

        def backtrack(row=0, col=0):
            """
            Backtracking
            """
            if board[row][col] != '.':
                move_to_next_cell_and_explore(row, col)
                return

            # The cell is empty.
            # Iterate over all numbers from 1 to 9.
            for d in range(1, 10):
                if could_place(d, row, col):  # (Constraints)
                    place_number(d, row, col)  # (Candidate)
                    move_to_next_cell_and_explore(row, col)  # (Explore)
                    if sudoku_solved:
                        # Sudoku is solved, there is no need to backtrack
                        # since the single unique solution is promised.
                        break

                    # Recover. (Backtracking)
                    remove_number(d, row, col)

        # box size
        n = 3
        # row size
        N = n * n
        # lambda function to compute box index
        def box_index(row, col): return (row // n) * n + col // n

        # Use dictionary for each row, column, and box to check if
        # there is a number already placed in there.
        # defaultdict(int) is common to be used to count something.
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        # Initialize the dictionaries.
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(d, i, j)

        sudoku_solved = False
        backtrack()


class Solution2:
    '''
    Use set, AC
    '''

    def __init__(self):
        pass

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def could_place(d, row, col):
            """
            Check if one could place a number d in (row, col) cell
            """
            return not (d in rows[row] or d in columns[col] or
                        d in boxes[box_index(row, col)])

        def place_number(d, row, col):
            """
            Place a number d in (row, col) cell
            """
            rows[row].add(d)
            columns[col].add(d)
            boxes[box_index(row, col)].add(d)
            board[row][col] = str(d)

        def remove_number(d, row, col):
            """
            Remove a number which didn't lead
            to a solution
            """
            rows[row].remove(d)
            columns[col].remove(d)
            boxes[box_index(row, col)].remove(d)
            board[row][col] = '.'

        def move_to_next(r, c):
            if c == N - 1:
                nr = r + 1
                nc = 0
            else:
                nr = r
                nc = c + 1

            return nr, nc

        def backtrack(r=0, c=0):
            while r != N and board[r][c] != '.':
                r, c = move_to_next(r, c)

            if r == N:
                # We're in the last cell, that means we have the solution.
                return True

            # Iterate over all numbers from 1 to 9.
            for d in range(1, 10):
                # (Constraints)
                if not could_place(d, r, c):
                    continue

                # (Candidate)
                place_number(d, r, c)
                nr, nc = move_to_next(r, c)
                if backtrack(nr, nc):  # (Explore further)
                    return True

                # Recover. (Backtracking)
                remove_number(d, r, c)

            return False

        # box size
        n = 3
        # row size
        N = n * n
        # lambda function to compute box index
        def box_index(row, col): return (row // n) * n + col // n

        # Use set for each row, column, and box to check if
        # there is a number already placed in there.
        rows = [set() for i in range(N)]
        columns = [set() for i in range(N)]
        boxes = [set() for i in range(N)]
        # Initialize the dictionaries.
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(d, i, j)

        # Let's get started.
        backtrack()


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_outputs = [
            # (input1, input2, expected output) depending on number of arguments
            ([["5", "3", ".", ".", "7", ".", ".", ".", "."],
              ["6", ".", ".", "1", "9", "5", ".", ".", "."],
              [".", "9", "8", ".", ".", ".", ".", "6", "."],
              ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
              ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
              ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
              [".", "6", ".", ".", ".", ".", "2", "8", "."],
              [".", ".", ".", "4", "1", "9", ".", ".", "5"],
              [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
             [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
              ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
              ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
              ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
              ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
              ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
              ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
              ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
              ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]),
        ]
        s = Solution2()
        for input1, expected in input_and_expected_outputs:
            with self.subTest(input1=input1, expected=expected):
                result = s.solveSudoku(input1)
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
