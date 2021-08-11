# Author: OldCodingFarmer + kei
# Date: August 10, 2021
from typing import *
from helper_classes import *


class Solution:
    # Top down - TLE
    def climbStairs1(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    # Bottom up, O(n) space
    def climbStairs2(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0 for i in range(n)]
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

    # Bottom up, O(1) space
    def climbStairs3(self, n: int) -> int:
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(2, n):
            tmp = b
            b = a + b
            a = tmp
        return b

    # Top down + memorization (list)
    def climbStairs4(self, n: int) -> int:
        if n == 1:
            return 1
        dic = [-1 for i in range(n)]
        dic[0], dic[1] = 1, 2
        return self.helper(n-1, dic)

    def helper(self, n, dic):
        if dic[n] < 0:
            dic[n] = self.helper(n-1, dic)+self.helper(n-2, dic)
        return dic[n]

    # Top down + memorization (dictionary)
    def __init__(self):
        self.dic = {1: 1, 2: 2}

    def climbStairs5(self, n: int) -> int:
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]

    def main():
        """ For testing """
        s = Solution()

        # Test args
        # nums = [3, 2, 5, 1]
        # target = 8
        # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
