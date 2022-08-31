# Author: leetcode + kei
# Date: July 15, 2021, August 30, 2022
import unittest
from helper_classes import *
from typing import *


class Solution:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 'head is None' is clearer than 'not head'.
        # By the way, 'not head' return True if head is an empty list.
        if head is None or head.next is None:
            return head
        # Assert that it has two or more nodes.

        # We only need one pointer.
        curr = head
        # repeat while curr node is not the last node
        while curr.next:
            if curr.val == curr.next.val:
                # Delete duplicate(next node).
                curr.next = curr.next.next
            else:
                # Move forward the pointer.
                curr = curr.next

        return head


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        n1 = ListNode(1)
        n2 = ListNode(1)
        n3 = ListNode(2)
        n1.next = n2
        n2.next = n3

        input_and_expected_outputs = [
            # (input1, input2, expected output) depending on number of arguments
            ([0, 1, 2], 3, 6),
            ([0, 1], 3, 5),
        ]
        s = Solution()
        for input1, input2, expected in input_and_expected_outputs:
            with self.subTest(input1=input1, input2=input2, expected=expected):
                result = s.deleteDuplicates(input1, input2)
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
    # unittest.main()
    n1 = ListNode(1)
    n2 = ListNode(1)
    n3 = ListNode(2)
    n1.next = n2
    n2.next = n3

    s = Solution()
    s.deleteDuplicates(n1)


if __name__ == '__main__':
    main()
