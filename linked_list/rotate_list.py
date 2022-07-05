# Author: leetcode + kei
# Date: July 4, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest


class Solution:
    def __init__(self):
        pass

    def rotateRight(
            self, head: Optional[ListNode],
            k: int) -> Optional[ListNode]:
        # No node or only one node
        if not head or not head.next:
            return head

        # Find the current tail and count the number of nodes in the list.
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        # close the linked list into the ring
        old_tail.next = head

        # Find the new tail first because we need to cut the circle later.
        # The new tail is:
        #   - 'n - 1 - k' ahead from head. (k < n)
        #   - 'n - 1 - (k % n)' ahead from head. (k >= n)
        new_tail = head
        for i in range(n - 1 - (k % n)):
            new_tail = new_tail.next

        # Get the new head.
        new_head = new_tail.next
        # break the ring
        new_tail.next = None

        return new_head


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
