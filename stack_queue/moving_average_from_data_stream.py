# Author: leetcode + kei
# Date: June 6, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest

from collections import deque


class Solution:
    '''
    Deque (Need import)
    First shot
    '''

    def __init__(self, size: int):
        self.win_size = size
        self.queue = deque()
        self.win_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        # Enqueue to the right anyway.
        self.queue.append(val)
        self.win_sum += val

        # Dequeue from the left when it's oversize.
        tail = self.queue.popleft() if self.count > self.win_size else 0
        self.win_sum -= tail

        return self.win_sum / min(self.count, self.win_size)


class Solution2:
    '''
    Circular Queue, Two Pointer
    Enqueue to tail and dequeue from head. (Other way around compared to Soluion3)
    Not for interview
    '''

    def __init__(self, size: int):
        self.win_size = size
        self.queue = [0] * self.win_size
        self.head = self.tail = 0
        self.win_sum = 0
        # number of elements seen so far
        self.count = 0

    def next(self, val: int) -> float:
        # When we say head or tail in a queue context, we need to define
        # what that means first. In this case, we enqueue to tail and
        # dequeue from head.

        # Do not dequeue until queue is full.
        if self.count >= self.win_size:
            # Dequeue from head first when queue is full.
            # Move forward the head.
            self.win_sum -= self.queue[self.head]
            self.head = (self.head + 1) % self.win_size

        # Enqueue to tail.
        # If the count >= winSize, then overwrite the oldest val.
        self.queue[self.tail] = val
        self.tail = (self.tail + 1) % self.win_size
        self.win_sum += val
        self.count += 1

        # Caluculate the average in the window.
        return self.win_sum / min(self.count, self.win_size)


class Solution3:
    '''
    Circular Queue without tail pointer
    Enqueue to head and dequeue from tail. (Other way around compared to Soluion2)
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

        # Dequeue from tail first.
        tail = (self.head + 1) % self.win_size
        # If 'count' is smaller than 'winSize', queue[tail] is 0.
        self.win_sum -= self.queue[tail]

        # Enqueue to head.
        # Move forward the head. If the count >= winSize, then
        # automatically remove/overwrite the oldest val.
        self.head = (self.head + 1) % self.win_size
        self.queue[self.head] = val
        self.win_sum += val

        # Caluculate the average in the window.
        return self.win_sum / min(self.count, self.win_size)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


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
