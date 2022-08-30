# Author: leetcode + kei
# Date: July 15, 2021, August 30, 2022
import unittest
from typing import *

from helper_classes import ListNode


class Solution:
    """
    1. Set
    O(N) time, O(N) space
    """

    def detectCycle(self, head):
        visited = set()
        node = head
        while node:
            if node in visited:
                return node
            visited.add(node)
            node = node.next

        # Despite the problem statement, it should be None.
        return None


class Solution2:
    """
    2. Two pointers (Floyd's Tortoise and Hare)
    O(N) time, O(1) space
    """

    def getIntersect(self, head: ListNode):
        slow = head
        fast = head

        # A fast pointer will either loop around a cycle and meet the slow
        # pointer or reach the None at the end of a non-cyclic list.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return fast

        return None

    def detectCycle(self, head: ListNode):
        if head is None:
            return None

        # If there is a cycle, the fast/slow pointers will intersect at some
        # node. Otherwise, there is no cycle, so we cannot find an entrance to
        # a cycle.
        intersect = self.getIntersect(head)
        if intersect is None:
            return None

        # To find the entrance to the cycle, we have two pointers traverse at
        # the same speed -- one from the front of the list, and the other from
        # the point of intersection.
        p1 = head
        p2 = intersect
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1


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
