# Author: leetcode + kei
# Date: July 24, 2021, September 17, 2022
import unittest
from typing import *
from helper_classes import *


class Solution:
    '''
    DFS recursive
    '''

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        D = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        R = len(grid)
        C = len(grid[0])

        def get_area(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or \
                    grid[r][c] == VISITED or grid[r][c] == WATER:
                return 0

            area = 1
            grid[r][c] = VISITED
            for d in D:
                area += get_area(r + d[0], c + d[1])

            return area

        max_area = 0
        WATER = 0
        ISLAND = 1
        VISITED = 2
        for r in range(R):
            for c in range(C):
                if grid[r][c] == ISLAND:
                    max_area = max(max_area, get_area(r, c))

        return max_area


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
