# Author: leetcode + kei
# Date: June 27, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest


class Solution:
    def __init__(self):
        pass

    def removeElements(
            self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # Dummy node is needed to make it simple to delete the first node.
        # because to delete a node in a singly linked list, we need a previous
        # pointer.
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head
        # A part of pattern to traverse the singly linked list to process the last node as well.
        while curr:
            if curr.val == val:
                # Delete the current node.
                prev.next = curr.next
            else:
                prev = curr
            # A part of pattern to traverse the singly linked list
            curr = curr.next

        # Not head because it might be deleted.
        return dummy.next


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
