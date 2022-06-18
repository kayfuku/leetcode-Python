# Author: leetcode + kei
# Date: June 17, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest


class Solution:
    '''
    Monotonic Stack
    A monotonic stack is simply a stack where the elements are always in sorted order.
    Monotonic stacks are a good option when a problem involves comparing
    the size of numeric elements, with their order being relevant.
    '''

    def __init__(self):
        pass

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        # Store indices.
        stack = []

        for curr_day, curr_temp in enumerate(temperatures):
            # Keep popping if curr_temp is warmer than the top of the stack.
            # This will also make sure that we find a next warmer day.
            # If the curr_temp is not warmer, then just push it.
            while stack and curr_temp > temperatures[stack[-1]]:
                # Pop the top of the stack because we found a warmer temp. Done with it.
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day

            # Push to wait until a warmer temp comes.
            stack.append(curr_day)

        return answer


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_outputs = [
            # (input, input, expected output) depending on number of arguments
            ([0, 1, 2], 3, 6),
            ([0, 1], 3, 5),
        ]
        s = Solution()
        for input1, input2, expected in input_and_expected_outputs:
            with self.subTest(input1=input1, input2=input2):
                result = s.solve(input1, input2)
                self.assertEqual(result, expected)

    def test_tree(self):
        '''
        Tree test example
        '''
        n1 = TreeNode(5)
        n2 = TreeNode(1)
        n3 = TreeNode(5)
        n4 = TreeNode(5)
        n5 = TreeNode(5)
        n6 = TreeNode(5)

        n1.left = n2
        n1.right = n3
        n3.right = n6
        n2.left = n4
        n2.right = n5

        s = Solution()
        result = s.countUnivalSubtrees(n1)
        self.assertEqual(result, 4)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
