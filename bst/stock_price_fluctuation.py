# Author: blackspinner + kei
# Date: May 10, 2022
import unittest
from typing import *
from helper_classes import *
import numpy as np

from sortedcontainers import SortedDict
from collections import *
import heapq


class Solution:

    def __init__(self):
        # SortedDict uses BST like TreeMap in Java.
        # K: timestamp, V: price, to get latest price
        self.time_to_price = SortedDict()
        # K: price, V: set of timestamps, to keep track of max and min of price
        # because same prices can come and updating can remove a price
        self.price_to_time_rec = SortedDict()

    def update(self, timestamp: int, price: int) -> None:
        # Remove old price.
        if timestamp in self.time_to_price:
            prev_price = self.time_to_price[timestamp]
            self.price_to_time_rec[prev_price].remove(timestamp)
            if len(self.price_to_time_rec[prev_price]) == 0:
                self.price_to_time_rec.pop(prev_price)

        # Set new price.
        if not price in self.price_to_time_rec:
            self.price_to_time_rec[price] = set()
        self.price_to_time_rec[price].add(timestamp)
        self.time_to_price[timestamp] = price

    def current(self) -> int:
        # Get latest price.
        # peekitem(): Optional argument index defaults to -1, the last item in the sorted dict.
        # Specify index=0 for the first item in the sorted dict.
        return self.time_to_price.peekitem(-1)[1]

    def maximum(self) -> int:
        # Get max price.
        return self.price_to_time_rec.peekitem(-1)[0]

    def minimum(self) -> int:
        # Get min price.
        return self.price_to_time_rec.peekitem(0)[0]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp, price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()


class Review:
    '''
    We use a BST instead of a heap because a heap takes O(N) time to remove an
    element while a BST only takes O(logN) time.
    '''

    def __init__(self):
        self.time_to_value = defaultdict(int)
        self.value_to_time = defaultdict(set)
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)
        self.latest_price = 0
        return

    def update(self, timestamp: int, price: int) -> None:
        old_price = self.time_to_value[timestamp]
        if len(self.value_to_time[old_price]) != 0:
            self.value_to_time[old_price].remove(timestamp)

        self.time_to_value[timestamp] = price
        self.value_to_time[price].add(timestamp)

        return

    def current(self) -> int:
        return self.latest_price

    def maximum(self) -> int:
        return heapq.heappop(self.max_heap)

    def minimum(self) -> int:
        return heapq.heappop(self.min_heap)


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
