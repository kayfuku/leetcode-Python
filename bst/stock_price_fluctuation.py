# Author: blackspinner + kei
# Date: May 10, 2022
from typing import *
from helper_classes import *
import numpy as np

from sortedcontainers import SortedDict


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


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 2
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
