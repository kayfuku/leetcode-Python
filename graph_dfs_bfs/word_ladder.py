# Author: leetcode + kei
# Date: September 19, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest


class Solution:
    '''
    1. BFS
    O(M^2*N) time, O(MN) space
    '''

    def ladderLength(
            self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        if end_word not in word_list:
            return 0

        # 1. Build a graph using Adjacency List.
        # Group words using wild card '*'. ex. hot => [*ot, h*t, ho*]
        # Adjacency List is good enough if you can get the neighbor nodes when you traverse.
        # Key does not have to be a node.
        # O(MN) time and space, where M is word length and N is list size.
        # K: generic word, V: a list of words which have the same intermediate generic word.
        map = defaultdict(list)
        L = len(begin_word)
        for word in word_list:
            for i in range(L):
                key = word[:i] + '*' + word[i + 1:]
                map[key].append(word)

        # 2. Do BFS
        # O(M^2*N) time because the number of nodes is MN and for each node,
        # it takes O(M) time
        # O(MN)space because of the queue
        # [word, level]
        queue = deque([(begin_word, 1)])
        # To make sure we don't repeat processing same word.
        visited = set([begin_word])
        while queue:
            current_word, level = queue.popleft()
            neighbors = self.get_neighbors(current_word, map)
            # neighbors
            for next_word in neighbors:
                if next_word == end_word:
                    return level + 1
                if next_word not in visited:
                    queue.append((next_word, level + 1))
                    visited.add(next_word)

        return 0

    def get_neighbors(self, word, map):
        '''
        O(M) time and space
        '''
        neighbors = []
        for i in range(len(word)):
            temp_word = word[:i] + "*" + word[i + 1:]
            # Note that map[temp_word] returns an empty list when temp_word is not
            # in the map. map.get(temp_word, []) also works.
            # But map.get(temp_word) does not work here
            # because begin_word might not be in the word_list and the map.
            temp_list = map[temp_word]
            neighbors.extend(temp_list)

        return neighbors


class Solution2:
    '''
    2. Bidirectional BFS
    '''

    def __init__(self):
        self.length = 0
        # K: generic word, V: a list of words which have the same intermediate generic word.
        self.map = defaultdict(list)

    def traverse(self, queue, visited, others_visited):
        queue_size = len(queue)
        for _ in range(queue_size):
            current_word = queue.popleft()
            for i in range(self.length):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in self.map[intermediate_word]:
                    # If the intermediate state/word has already been visited from the
                    # other parallel traversal this means we have found the answer.
                    if word in others_visited:
                        return visited[current_word] + others_visited[word]
                    if word not in visited:
                        # Save the level as the value of the dictionary, to save number of hops.
                        visited[word] = visited[current_word] + 1
                        queue.append(word)

        return None

    def ladderLength(self, begin_word, end_word, word_list):
        if end_word not in word_list:
            return 0

        self.length = len(begin_word)

        for word in word_list:
            for i in range(self.length):
                self.map[word[:i] + "*" + word[i+1:]].append(word)

        # Bidirectional BFS
        queue_begin = deque([begin_word])
        visited_begin = {begin_word: 1}
        queue_end = deque([end_word])
        visited_end = {end_word: 1}
        ans = None

        # TODO:
        # We do a birdirectional search starting one pointer from begin
        # word and one pointer from end word. Hopping one by one.
        while queue_begin and queue_end:

            # Progress forward one step from the shorter queue
            if len(queue_begin) <= len(queue_end):
                ans = self.traverse(queue_begin, visited_begin, visited_end)
            else:
                ans = self.traverse(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
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
