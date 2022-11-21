# Author: leetcode + kei
# Date: May 28, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest


class Logger:

    def __init__(self):
        # K: message, V: next allowed timestamp
        self._msg_dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self._msg_dict:
            self._msg_dict[message] = timestamp + 10
            return True

        next_allowed_time = self._msg_dict[message]
        if timestamp >= next_allowed_time:
            self._msg_dict[message] = timestamp + 10
            return True

        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

class Review:

    def __init__(self):
        self.mp = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.mp:
            self.mp[message] = timestamp + 10
            return True

        if timestamp >= self.mp[message]:
            self.mp[message] = timestamp + 10
            return True

        return False


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
        s = Logger()
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
