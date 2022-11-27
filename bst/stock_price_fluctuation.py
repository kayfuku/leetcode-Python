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
        self.price_to_time_list = SortedDict()

    def update(self, timestamp: int, price: int) -> None:
        # Remove old price from price_to_time_list.
        if timestamp in self.time_to_price:
            old_price = self.time_to_price[timestamp]
            self.price_to_time_list[old_price].remove(timestamp)
            if len(self.price_to_time_list[old_price]) == 0:
                self.price_to_time_list.pop(old_price)

        # Save new price in price_to_time_list and time_to_price.
        self.time_to_price[timestamp] = price
        if not price in self.price_to_time_list:
            self.price_to_time_list[price] = set()
        self.price_to_time_list[price].add(timestamp)

    def current(self) -> int:
        # Get latest price.
        # peekitem(): Optional argument index defaults to -1, the last item in the sorted dict.
        return self.time_to_price.peekitem(-1)[1]

    def maximum(self) -> int:
        # Get max price.
        return self.price_to_time_list.peekitem(-1)[0]

    def minimum(self) -> int:
        # Get min price.
        # Specify index=0 for the first item in the sorted dict.
        return self.price_to_time_list.peekitem(0)[0]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp, price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()


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
