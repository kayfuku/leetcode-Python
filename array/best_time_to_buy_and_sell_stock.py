# Author: girikuncoro + kei
# Date: August 9, 2021
from typing import *
from helper_classes import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')
        for p in prices:
            # update min so far
            if p < min_price:
                min_price = p
            else:
                # calc profit
                profit = p - min_price
                # take max
                max_profit = max(max_profit, profit)

        return max_profit


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 8
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
