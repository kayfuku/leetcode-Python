# Author: leetcode + kei
# Date: November 9, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest

import heapq


class Solution:
    '''
    1. Using Min-Heap. (This is good enough)
    First, sort by the start time, and then put it in the Min-Heap
    to know the earliest end time of the ongoing meetings.
    O(NlogN) time, since the for-loop iterates N times, and for each iteration,
    peek() takes O(1) time, poll() takes O(logN) time, and offer() takes O(logN)
    time.
    O(N) space, in the worst case, all the N meetings are in the heap.
    '''

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Sort the meetings in increasing order by their start time.
        intervals.sort(key=lambda x: x[0])

        # Create a Min-heap to know the earliest end time of the ongoing meetings.
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][1])

        for intvl in intervals[1:]:
            # Check the earliest end time of ongoing meetings.
            # free_rooms[0] is a peek() of the heap.
            if free_rooms[0] <= intvl[0]:
                # The start time is later than or equal to the earliest end time.
                # No overlapped. Let's use that room.
                # Delete the old one (the meeting has finished), and
                # update the earliest end time in the heap.
                # The heap size (the number of rooms needed) does not change for this
                # iteration.
                heapq.heappop(free_rooms)

            # Add the end time of the current meeting to the heap.
            heapq.heappush(free_rooms, intvl[1])

        # The heap size is the number of the meeting rooms needed.
        # Can you imagine why the heap size after the iterations is the maximum number
        # of overlapped meetings (minimum number of rooms required)?
        # This is the most important point.
        # Even if a meeting finishes, the meeting will not be deleted unless we add a
        # new meeting in substitution for the meeting. Thus, the maximum number of
        # overlapped meetings is persistent.
        return len(free_rooms)


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        Change input and expected output as needed.
        '''
        input_and_expected_output = [
            # (input1, input2, expected output) depending on number of arguments
            ([0, 1, 2], 3, 6),
            ([0, 1], 3, 5),
        ]
        s = Solution()
        for case, (input1, input2, expected) in enumerate(
                input_and_expected_output):
            print('Case: {}'.format(case))
            with self.subTest(input1=input1, input2=input2, expected=expected):
                # Change to the method name to be tested.
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
