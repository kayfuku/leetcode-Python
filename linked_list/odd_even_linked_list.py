# Author: leetcode + kei
# Date: June 28, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest


class Solution:
    def __init__(self):
        pass

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            # head is None or an empty list.
            return head
        # Assert head has at least one node.

        odd = head
        even = head.next
        # Keep this point and the last node in the odd list linkes to this.
        even_head = head.next
        # when even gets to the last node or last None, which means
        # the even list ends, stop traversing.
        while even and even.next:
            # Move forward odd first skipping the even.
            odd.next = even.next
            odd = odd.next
            # Then move forward even skipping the odd.
            even.next = odd.next
            even = even.next

        # Connect the last node in the odd list to the even head.
        odd.next = even_head

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
