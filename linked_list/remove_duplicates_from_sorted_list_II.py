# Author: + kei
# Date: July ?, 2021, August 31, 2022
import unittest
from typing import *
from helper_classes import *


class Solution:
    '''
    Two pointers
    '''

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        # 'slow' is always the last node of the desired list.
        slow = dummy
        fast = head

        while fast:
            # Move 'fast' till the end of duplicates sublist.
            while fast.next and fast.val == fast.next.val:
                fast = fast.next

            if slow.next != fast:
                # Delete all the duplicates from 'slow.next' to 'fast'.
                slow.next = fast.next
                fast = slow.next
            else:
                # 'fast' and 'fast.next' is not the same because 'fast' has not moved
                # from 'slow.next', which means 'fast' is a distinct number.
                # Move forward both pointers by one.
                slow = slow.next
                fast = fast.next

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
    #     result = s.countUnivalSubtrees(n1)
    #     self.assertEqual(result, 4)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
