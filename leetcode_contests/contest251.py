# Author: leetcode + kei
# Date: July ?, 2021
from typing import *
from helper_classes import *


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = []
        for c in s:
            num = ord(c) - ord('a') + 1
            nums.append(str(num))

        nums = int(''.join(nums))
        while k > 0:
            sum = 0
            while nums > 0:
                sum += nums % 10
                nums //= 10
            nums = sum
            k -= 1

        return sum

    def maximumNumber(self, num: str, change: List[int]) -> str:
        ret = []
        stop = False
        flag = 'num'
        for d in num:
            if stop or int(d) > change[int(d)] or (True
                                                   if int(d) == change[int(d)] and flag == 'num' else False):
                ret.append(d)
                if flag == 'c':
                    stop = True
            else:
                ret.append(str(change[int(d)]))
                flag = 'c'

        return ''.join(ret)

    def maxCompatibilitySum(self, students: List[List[int]],
                            mentors: List[List[int]]) -> int:
        n = len(students[0])
        score_mat = [[]]
        for i, stu in students:
            for j, men in mentors:
                score = 0
                for k in range(n):
                    if students[i][k] == mentors[j][k]:
                        score += 1
                score_mat[i][j] = score

        return


def main():
    """ For testing """
    solution = Solution()

    # Test args
    s = "leetcode"
    k = 2
    print(solution.getLucky(s, k))


if __name__ == '__main__':
    main()
