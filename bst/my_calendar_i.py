# Author: leetcode + kei
# Date: November 14, 2022
from sortedcontainers import SortedList
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class MyCalendar:
    '''
    O(N^2) time, O(N) space
    '''

    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        for s, e in self.calendar:
            if not (start >= e or s >= end):
                return False

        self.calendar.append((start, end))
        return True


class MyCalendar2:
    '''
    BST and Binary Search
    Good for interview
    O(NlogN) time, O(N) space
    '''

    def __init__(self):
        from sortedcontainers import SortedList
        # SortedList is like a TreeSet in Java, which is made of balanced Binary Search Tree.
        self.sorted_list = SortedList()

    def book(self, start: int, end: int) -> bool:
        # bisect_left() returns index of x if x is in the list.
        # If x is not in the list, then it returns index at which x would be.
        # That means that the element at the index is greater than x.
        # Thus, self.sorted_list[idx] refers to the next meeting.
        # Be careful to avoid index out of bounds because idx could be 0 or len(self.calender).
        idx = self.sorted_list.bisect_left((start, end))

        # This meeting must start after previous meeting ends.
        # Check with the end time of previous meeting.
        if (idx > 0 and start < self.sorted_list[idx - 1][1]):
            # Overlapped because the start time of this meeting is earlier than
            # the end time of previous meeting.
            return False

        # This meeting must end before next meeting starts.
        # Check with the start time of next meeting.
        if (idx < len(self.sorted_list) and end > self.sorted_list[idx][0]):
            # Overlapped because the end time of this meeting is later than
            # the start time of next meeting.
            return False

        # If there is no overlapped meetings, then add this meeting to the sorted list.
        # Tuples are sorted based on the first element in SortedList.
        # That means that the meetings are sorted by their start time.
        self.sorted_list.add((start, end))

        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


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
        s = MyCalendar()
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
