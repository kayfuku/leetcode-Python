# Author: leetcode + kei
# Date: June 6, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest


class Solution:
    '''
    List
    '''

    def __init__(self, size: int):
        self.win_size = size
        self.queue = []

    def next(self, val: int) -> float:
        win_size, queue = self.win_size, self.queue
        queue.append(val)
        # calculate the sum of the moving window
        win_sum = sum(queue[-win_size:])

        # Calculate average.
        # Queue size can be smaller or larger than the window size.
        return win_sum / min(len(queue), win_size)

# TODO: Deque


class Solution3:
    '''
    Circular Queue
    Not for interview
    '''

    def __init__(self, size: int):
        self.win_size = size
        self.queue = [0] * self.win_size
        self.head = self.win_sum = 0
        # number of elements seen so far
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        # When we say head or tail in a queue context, we need to define
        # what that means first. In this case, we enqueue to head and
        # dequeue from tail.

        # Dequeue from tail.
        tail = (self.head + 1) % self.win_size
        self.win_sum = self.win_sum - self.queue[tail] + val
        # Enqueue to head.
        self.head = (self.head + 1) % self.win_size
        self.queue[self.head] = val

        # Caluculate the average.
        return self.win_sum / min(self.win_size, self.count)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


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
