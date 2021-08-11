# Author: leetcode + kei
# Date: August 10, 2021
from typing import *
from helper_classes import *
import numpy as np


class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        curr = head
        while curr is not None:
            vals.append(curr.val)
            curr = curr.next
        return vals == vals[::-1]


class Solution2:

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        # first_half_end.next is like this
        # 1-2-3-3-2-1 => 3-2-1
        # 1-2-3-2-1 => 2-1
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        p1 = head
        p2 = second_half_start
        while result and p2 is not None:
            if p1.val != p2.val:
                result = False
            p1 = p1.next
            p2 = p2.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 2
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
