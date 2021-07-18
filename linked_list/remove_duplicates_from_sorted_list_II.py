# Author: + kei
# Date: July ?, 2021
from typing import *
from helper_classes import *


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        # before the sublist of duplicates
        slow = dummy
        fast = head

        while fast:
            # move till the end of duplicates sublist
            while fast.next and fast.val == fast.next.val:
                fast = fast.next

            if slow.next != fast:
                # skip all duplicates
                slow.next = fast.next
                fast = slow.next
            else:
                slow = slow.next
                fast = fast.next

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
