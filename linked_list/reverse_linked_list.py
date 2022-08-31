# Author: leetcode + kei
# Date: July 16, 2021, August 31, 2022
import unittest
from typing import *
from helper_classes import *


class Solution:
    '''
    Iterative, good for interview
    '''

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            # First, we need next node so that curr pointer can move to the node
            # after the link is cut.
            next_node = curr.next
            # Reverse the link.
            curr.next = prev
            # Move on to the next.
            prev = curr
            curr = next_node

        # If the head is an empty list, then prev is None, which is ok
        # despite the problem statement.
        return prev


class Solution2:
    '''
    Recursive
    '''

    def reverseList(self, head: ListNode) -> ListNode:

        def helper(prev, curr: ListNode) -> ListNode:
            if curr is None:
                return prev

            next_node = curr.next
            curr.next = prev

            # prev gets curr and curr gets next_node in the next recursion stack.
            return helper(curr, next_node)

        prev = None
        # Each recursion stack takes as input two pointers, prev and curr.
        return helper(prev, head)


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
