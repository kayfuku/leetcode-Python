# Author: leetcode + kei
# Date: July 3, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    '''
    DFS recursive
    '''

    def __init__(self):
        # We need 'visited' dict because we traverse like a graph.
        # K: old node, V: new node
        self.visited = {}

    def copyRandomList(self, node: Optional[Node]) -> Optional[Node]:
        if node == None:
            return None

        # If we have already processed the current node, then
        # we simply return the cloned version of it.
        if node in self.visited:
            return self.visited[node]

        # Create a new node with the same value as old node.
        new_node = Node(node.val, None, None)

        # Save this value in the hash map. This is needed since there might be
        # loops during traversal due to randomness of random pointers and
        # this would help us avoid them.
        self.visited[node] = new_node

        # Recursively copy the remaining linked list starting once from
        # the next pointer and then from the random pointer.
        # Thus we have two independent recursive calls.
        # Finally we update the next and random pointers for the new node created.
        new_node.next = self.copyRandomList(node.next)
        new_node.random = self.copyRandomList(node.random)

        return new_node


class Solution2(object):
    '''
    DFS iterative
    '''

    def __init__(self):
        # We need 'visited' dict because we traverse like a graph.
        # K: old node, V: new node
        self.visited = {}

    def getClonedNode(self, node):
        if not node:
            return None

        if node in self.visited:
            return self.visited[node]

        new_node = Node(node.val, None, None)
        self.visited[node] = new_node
        return new_node

    def copyRandomList(self, head):
        if not head:
            return head

        node = head
        # Creating the new head node.
        new_node = Node(node.val, None, None)
        self.visited[node] = new_node

        # Iterate on the linked list until all nodes are cloned.
        while node != None:
            new_node.next = self.getClonedNode(node.next)
            new_node.random = self.getClonedNode(node.random)

            # Move one step ahead in the linked list.
            node = node.next
            new_node = new_node.next

        return self.visited[head]


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
