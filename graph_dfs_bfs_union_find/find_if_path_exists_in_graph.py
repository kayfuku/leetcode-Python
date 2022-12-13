# Author: leetcode + kei
# Date: December 7, 2022
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
    BFS
    O(V + E) time and space, where V is the number of nodes and E is the number of edges.
    '''

    def validPath(
            self, n: int, edges: List[List[int]],
            source: int, destination: int) -> bool:

        # Graph with Adjacency List
        g = defaultdict(set)
        for e in edges:
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])

        def bfs(src):
            q = deque([src])
            seen = set([src])
            while q:
                node = q.popleft()
                if node == destination:
                    return True
                for nei in g[node]:
                    if nei not in seen:
                        q.append(nei)
                        seen.add(nei)

            return False

        return bfs(source)

    def validPath2(
            self, n: int, edges: List[List[int]],
            source: int, destination: int) -> bool:
        '''
        print the shortest path
        '''

        # Graph with Adjacency List
        g = defaultdict(set)
        for e in edges:
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])

        def bfs(src):
            path = []
            path.append(src)
            q = deque([path])
            seen = set([src])
            while q:
                path = q.popleft()
                node = path[-1]
                if node == destination:
                    print(path)
                    return True
                for nei in g[node]:
                    if nei not in seen:
                        path.append(nei)
                        q.append(list(path))
                        seen.add(nei)
                        path.pop()

            return False

        return bfs(source)


class Solution:
    '''
    DFS
    O(V + E) time and space, where V is the number of nodes and E is the number of edges.
    '''

    def validPath(
            self, n: int, edges: List[List[int]],
            source: int, destination: int) -> bool:

        # Graph with Adjacency List
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(src, dst):
            if src == dst:
                return True
            seen.add(src)
            for nei in g[src]:
                if nei not in seen:
                    if dfs(nei, dst):
                        return True
            return False

        seen = set()
        return dfs(source, destination)


class Solution3:
    '''
    Union Find
    O(E・α(V)) time and O(V) space, where α is an Inverse Ackermann Function.
    '''

    def validPath(
            self, n: int, edges: List[List[int]],
            source: int, destination: int) -> bool:
        uf = UF(n)
        for u, v in edges:
            uf.unite(u, v)

        return uf.is_connected(source, destination)


class UF:
    def __init__(self, n):
        self.n = n
        self.roots = [i for i in range(n)]

    def find(self, x):
        if self.roots[x] == x:
            return x
        return self.find(self.roots[x])

    def unite(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        self.roots[root_x] = root_y
        return True

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Try:

    def solve(self, nums: List[int], target: int) -> List[int]:
        return 0


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
