# Author: leetcode + kei
# Date: July 1, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest


class Node:
    # We can use construct to link to the next node.
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:

    def insert(self, head: Node, insert_val: int) -> Node:
        if head is None:
            new_node = Node(insert_val, None)
            # Create a single circular list.
            new_node.next = new_node
            return new_node

        prev = head
        curr = head.next
        # Note that you cannnot put curr != head.next here to check the last
        # interval between the head and the tail. Insert it later.
        while curr != head:

            if prev.val <= insert_val <= curr.val:
                # Case #1.
                # Don't forget to put the curr in to make it circular.
                prev.next = Node(insert_val, curr)
                return head
            elif prev.val > curr.val:
                # Case #2. where we locate the max (prev.val) in the sorted list.
                if insert_val >= prev.val or insert_val <= curr.val:
                    # insert_val is a new max or min in the list.
                    prev.next = Node(insert_val, curr)
                    return head

            prev = curr
            curr = curr.next

        # Case #3.
        # The insert_val is in the last interval between the head and the tail
        # whatever the value is.
        # The value could be prev <= insert_val <= curr if the head is not min or
        # max in the list.
        # The value could be a new min or max if the head is min in the list.
        prev.next = Node(insert_val, curr)

        return head


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
    #     result = s.solve(n1)
    #     self.assertEqual(result, 4)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
