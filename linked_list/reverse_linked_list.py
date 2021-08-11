# Author: leetcode + kei
# Date: July 16, 2021
from typing import *
from helper_classes import *


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """ iterative """
        prev = None
        curr = head
        while curr:
            # new node
            next_node = curr.next
            # reverse the link
            curr.next = prev
            # move on to the next
            prev = curr
            curr = next_node

        return prev


class Solution2:

    def helper(self, prev, curr):
        if curr is None:
            return prev

        next_node = curr.next
        curr.next = prev

        return self.helper(curr, next_node)

    def reverseList(self, head: ListNode) -> ListNode:
        """ recursive """
        prev = None
        return self.helper(prev, head)


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 8
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
