# Author: leetcode + kei
# Date: June 29, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest


class Node:
    '''
    Definition for the special node.
    Overwrite the Node class in the helper_classes.
    '''

    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    '''
    DFS recursive
    '''

    def __init__(self):
        pass

    def flatten(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return head

        # Dummy node to ensure the 'prev' pointer is never None
        # becausee prev.next is used in the function.
        dummy_node = Node(0, None, head, None)
        self.flatten_dfs(dummy_node, head)

        # Detach the dummy node from the real head.
        dummy_node.next.prev = None
        return dummy_node.next
        # This is also ok.
        # head.next = None
        # return head

    def flatten_dfs(self, prev: Node, curr: Node) -> Node:
        """ return the tail of the flatten list """
        if not curr:
            return prev

        # Connect prev and curr nodes with each other using their next and prev
        # pointer respectively. Note that child pointer is not changed.
        prev.next = curr
        curr.prev = prev

        # Keep curr.next because it would be changed in the recursive function.
        temp_next = curr.next
        # Flatten left subtree and connect it to the curr node.
        tail_left = self.flatten_dfs(curr, curr.child)
        # Detach the left subtree.
        curr.child = None
        # Flatten right subtree and connect it to the tail_left.
        tail_right = self.flatten_dfs(tail_left, temp_next)

        return tail_right


class Solution2(object):
    '''
    DFS iterative
    '''

    def flatten(self, head):
        if not head:
            return

        dummy_head = Node(0, None, head, None)
        prev = dummy_head

        stack = []
        stack.append(head)

        while stack:
            curr = stack.pop()

            prev.next = curr
            curr.prev = prev

            # Right subtree first!
            if curr.next:
                stack.append(curr.next)

            # Then, leftsubtee.
            if curr.child:
                stack.append(curr.child)
                # don't forget to remove all child pointers.
                curr.child = None

            prev = curr

        # detach the pseudo head node from the result.
        dummy_head.next.prev = None

        return dummy_head.next


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
