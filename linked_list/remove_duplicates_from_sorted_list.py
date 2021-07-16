# Author: leetcode + kei
# Date: July 15, 2021
from typing import *


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        curr = head
        # repeat while curr node is not the last node
        while curr.next is not None:
            if curr.val == curr.next.val:
                # delete duplicate
                curr.next = curr.next.next
            else:
                # keep curr node
                curr = curr.next

        return head


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 8
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
