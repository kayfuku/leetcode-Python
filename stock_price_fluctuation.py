# Author: leetcode + kei
# Date: May 10, 2022
from typing import *
from helper_classes import *
import numpy as np


class Solution:
    def __init__(self):
        self.records = []

    def update(self, timestamp: int, price: int) -> None:
        pass

    def current(self) -> int:
        pass

    def maximum(self) -> int:
        pass

    def minimum(self) -> int:
        pass

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
