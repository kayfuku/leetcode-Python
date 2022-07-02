# Author: leetcode + kei
# Date: July 1, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest


class Node:
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

        # TODO:
        prev = head
        curr = head.next
        to_insert = False

        while curr != head:

            if prev.val <= insert_val <= curr.val:
                # Case #1.
                to_insert = True
            elif prev.val > curr.val:
                # Case #2. where we locate the tail element
                # 'prev' points to the tail, i.e. the largest element!
                if insert_val >= prev.val or insert_val <= curr.val:
                    to_insert = True

            if to_insert:
                prev.next = Node(insert_val, curr)
                # mission accomplished
                return head

            prev = curr
            curr = curr.next

        # Case #3.
        # did not insert the node in the loop
        # Every node in the list is the same value.
        # insert_val is less than or greater than that value.
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
