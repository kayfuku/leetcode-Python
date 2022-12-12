# Author: leetcode + kei
# Date: December 11, 2022
from typing import *
from helper_classes import *
from collections import defaultdict, deque
from sortedcontainers import SortedList, SortedSet, SortedDict
import bisect
import heapq
import numpy as np
import unittest


class Solution:
    '''
    DFS, Backward edge detection in a directed graph
    There are three status of a node, "never seen", "processing", and "leads to dst".
    Author: reddddddd + kei
    '''

    def leadsToDestination(
            self, n: int, edges: List[List[int]],
            source: int, destination: int) -> bool:
        g = defaultdict(set)
        leads_to_dst = defaultdict(int)
        for [x, y] in edges:
            g[x].add(y)

        PROCESSING = -1
        LEADS_TO_DST = 1

        def dfs(node):
            # Note that leads_to_dst[node] is 0 if the node has never been seen.
            if leads_to_dst[node] == LEADS_TO_DST:
                # This node leads to the destination.
                return True
            if leads_to_dst[node] == PROCESSING:
                # There is a backward edge in the directed graph.
                return False
            if len(g[node]) == 0:
                # The node has no out-edge.
                return node == destination
            # Assert that the node is new and has at least one out-edge.

            leads_to_dst[node] = PROCESSING
            for nei in g[node]:
                # Check all neighbor nodes regardless of whether it's visited.
                # Return False if the node has at least one backward edge.
                if not dfs(nei):
                    return False
            # Assert that the node does not have a backward edge and
            # leads to the destination.

            leads_to_dst[node] = LEADS_TO_DST
            return True

        return dfs(source)


class Try:
    '''
    WA for this problem, but it's useful for other problem, which is like
    to return True if all the paths lead eventually to destination even if
    there is a cycle in the graph.
    '''

    def leadsToDestination(
            self, n: int, edges: List[List[int]],
            source: int, destination: int) -> bool:
        # Create a directed graph.
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)

        def dfs(node, dst):
            if node == dst:
                leads_to_dst[node] = True
                return True

            leads_to_dst[node] = False
            for nei in g[node]:
                if nei not in leads_to_dst:
                    if not dfs(nei, dst):
                        # We found the path that does not lead to dst.
                        return False
                    else:
                        leads_to_dst[node] = True

                elif leads_to_dst[nei]:
                    leads_to_dst[node] = True
                    return True

            return leads_to_dst[node]

        leads_to_dst = {}
        return dfs(source, destination)


class Bot:

    def solve(self, nums: List[int], target: int) -> List[int]:
        return 0


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        Change input and expected output as needed.
        '''
        input_and_expected_output = [
            # (input1, input2, expected output) depending on number of arguments
            ([0, 1, 2], 3, 6),
            ([0, 1], 3, 5),
        ]
        s = Solution()
        for case, (input1, input2, expected) in enumerate(
                input_and_expected_output):
            print('Case: {}'.format(case))
            with self.subTest(input1=input1, input2=input2, expected=expected):
                # Change to the method name to be tested.
                result = s.topKFrequent(input1, input2)
                self.assertEqual(result, expected)

    # def test_tree(self):
    #     '''
    #     Tree test example
    #     '''
    #     # Binary Tree
    #     #     6
    #     #    /  \
    #     #   3    12
    #     #  / \   / \
    #     # 1   4 9  14

    #     n1 = TreeNode(6)
    #     n2 = TreeNode(3)
    #     n3 = TreeNode(12)
    #     n4 = TreeNode(1)
    #     n5 = TreeNode(4)
    #     n6 = TreeNode(9)
    #     n7 = TreeNode(14)

    #     n1.left = n2
    #     n1.right = n3
    #     n2.left = n4
    #     n2.right = n5
    #     n3.left = n6
    #     n3.right = n7

    #     s = Solution()
    #     input_and_expected_outputs = [
    #         # (input1, input2, expected output) depending on number of arguments
    #         (n1, n6, n7, n3),
    #         (n1, n3, n5, n1),
    #         (n1, n4, n5, n1),  # Fail
    #     ]
    #     s = Solution()
    #     for input1, input2, input3, expected in input_and_expected_outputs:
    #         with self.subTest(input1=input1.val, input2=input2.val, input3=input3.val,
    #                           expected=expected.val):
    #             result = s.solve(input1, input2, input3)
    #             self.assertEqual(result, expected)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
