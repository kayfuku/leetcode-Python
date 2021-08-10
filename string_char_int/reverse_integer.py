# Author: leetcode + kei
# Date: August 9, 2021
from typing import *
from helper_classes import *


class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = 1
        if x < 0:
            x = -x
            sign = -1

        while x:
            pop = x % 10
            x //= 10
            if sign == 1:
                if rev > (pow(2, 31) - 1) // 10 or rev == (pow(2, 31) - 1) // 10 and pop > 7:
                    return 0
            else:
                if rev > pow(2, 31) // 10 or rev == pow(2, 31) // 10 and pop > 8:
                    return 0
            rev = rev * 10 + pop

        return rev if sign == 1 else rev * sign


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 8
    # print(s.solve(nums, target))
    x = 1534236469
    print(s.reverse(x))


if __name__ == '__main__':
    main()
