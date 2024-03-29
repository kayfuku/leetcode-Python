# Author: leetcode + kei
# Date: June 19, 2022, December 10, 2022
from collections import deque
from typing import *
from helper_classes import *
import numpy as np
import unittest


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    '''
    DFS
    Good for interview
    '''

    def __init__(self):
        # Dictionary to save the visited node and its respective clone
        # as key and value respectively. This helps to avoid cycles.
        # K: visited node, V: cloned node
        # In general, when we traverse a graph, we need 'visited/seen' dict.
        self.visited = {}

    def cloneGraph(self, node: Node) -> Node:
        # If we access node.val later on, then we need null check.
        if node is None:
            return node

        # If the node was already visited before,
        # return the clone from the visited dictionary.
        # Memoization
        if node in self.visited:
            return self.visited[node]

        # Create a clone for the given node.
        clone_node = Node(node.val, [])
        # Memoization
        self.visited[node] = clone_node

        # Iterate through the neighbors to generate their clones
        # and prepare a list of cloned neighbors to be added to the cloned node.
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node


class Solution2(object):
    '''
    BFS
    A bit hard for interview
    '''

    def cloneGraph(self, node):
        if node is None:
            return node

        # Dictionary to save the visited node and its respective clone
        # as key and value respectively. This helps to avoid cycles.
        visited = {}

        # BFS
        queue = deque([node])
        # Clone the node and put it in the visited dictionary.
        visited[node] = Node(node.val, [])
        while queue:
            n = queue.popleft()

            # Iterate through all the neighbors of the node
            for nei in n.neighbors:
                if nei not in visited:
                    # Clone the neighbor and put in the visited.
                    visited[nei] = Node(nei.val, [])
                    # Add the newly encountered node to the queue.
                    queue.append(nei)

                # Add the clone of the neighbor to the neighbors of the clone node "n".
                visited[n].neighbors.append(visited[nei])

        # Return the clone of the node from visited.
        return visited[node]


class Review:
    '''
    DFS
    Good for interview
    '''

    def cloneGraph(self, root: Node) -> Node:
        # K: node, V: cloned node
        map = {}

        def dfs(node):
            # If we access node.val later on, then we need null check here.
            if node is None:
                return None

            if node in map:
                return map[node]

            c_node = Node(node.val)
            map[node] = c_node

            for nei in node.neighbors:
                c_nei = dfs(nei)
                c_node.neighbors.append(c_nei)

            return c_node

        c_root = dfs(root)
        return c_root


class Review2:
    '''
    BFS
    '''

    def cloneGraph(self, node: Node) -> Node:
        if node is None:
            return node

        # K: node, V: cloned node
        map = {}

        q = deque([node])
        # dict not set because we need to return the cloned node
        map[node] = Node(node.val)
        while q:
            curr = q.popleft()
            for nei in curr.neighbors:
                if nei not in map:
                    q.append(nei)
                    # Create the cloned node.
                    map[nei] = Node(nei.val)

                # Don't forget this!! This is a bit different from other BFS problems.
                # Connect the (already) cloned neighbor node whether or not it's visited.
                map[curr].neighbors.append(map[nei])

        return map[node]


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
