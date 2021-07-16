# Author: leetcode + kei
# Date: July 15, 2021
from typing import *


class Solution:
    """
    Set
    O(N) time, O(N) space
    """

    def detectCycle(self, head):
        visited = set()
        node = head
        while node is not None:
            if node in visited:
                return node
            visited.add(node)
            node = node.next

        return None


class Solution2:
    """
    Two pointers
    O(N) time, O(1) space
    """

    def getIntersect(self, head):
        slow = head
        fast = head

        # A fast pointer will either loop around a cycle and meet the slow
        # pointer or reach the `null` at the end of a non-cyclic list.
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return fast

        return None

    def detectCycle(self, head):
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


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 8
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
