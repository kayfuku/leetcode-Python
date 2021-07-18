# Author: leetcode + kei
# Date: July 16, 2021
from typing import *
from helper_classes import *


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next

        if carry:
            curr.next = ListNode(carry)

        return dummy.next


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 8
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
