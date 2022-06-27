# Author: leetcode + kei
# Date: July ?, 2021
import unittest
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
