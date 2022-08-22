# Author: leetcode + kei
# Date: August 22, 2022
from typing import *
from helper_classes import *
from collections import *
import numpy as np
import unittest

from random import choice


class RandomizedSet():
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Insert a value to the set.
        Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False

        # Add it at the tail in the list.
        self.list.append(val)
        # We need to keep track of indices of vals using dict in order to delete
        # them in O(1) time.
        # We need to be careful about putting the index in the dict because the
        # size changes once adding it.
        # len(self.list) - 1 indicates the last index of the array.
        self.dict[val] = len(self.list) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set.
        Returns true if the set contained the specified element.
        """
        if val not in self.dict:
            return False

        # Copy the last element to the val to be deleted in the list and then
        # delete the last element later.
        # If you remove without moving the val to the last element, then shifting will
        # occur, which takes O(N) time.
        last_element = self.list[-1]
        # This is exactly why we need a dict for this problem. When we know the element
        # to be deleted but don't know the index, we cannot copy over to it in O(1)
        # time.
        idx = self.dict[val]
        self.list[idx] = last_element
        # Update the index of the copied element.
        self.dict[last_element] = idx
        # Delete the last element
        self.list.pop()
        del self.dict[val]

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # We have to use a list in order to be able to randomly pick up one element.
        # That's why we use a list, not a set.
        # Then, when we implement remove() that only takes O(1) time, we have to
        # use a hash table to do lookup in O(1) time.
        return choice(self.list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


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
        s = RandomizedSet()
        for input1, input2, expected in input_and_expected_outputs:
            with self.subTest(input1=input1, input2=input2, expected=expected):
                result = s.solve(input1, input2)
                self.assertEqual(result, expected)

    # def test_tree(self):
    #     '''
    #     Tree test example
    #     '''
    #     # Binary Tree
    #     #     6
    #     #    /  \
    #     #   3    12
    #     #  / \   / \
    #     # 1   4 9  14

    #     n1 = TreeNode(6)
    #     n2 = TreeNode(3)
    #     n3 = TreeNode(12)
    #     n4 = TreeNode(1)
    #     n5 = TreeNode(4)
    #     n6 = TreeNode(9)
    #     n7 = TreeNode(14)

    #     n1.left = n2
    #     n1.right = n3
    #     n2.left = n4
    #     n2.right = n5
    #     n3.left = n6
    #     n3.right = n7

    #     s = Solution()
    #     input_and_expected_outputs = [
    #         # (input1, input2, expected output) depending on number of arguments
    #         (n1, n6, n7, n3),
    #         (n1, n3, n5, n1),
    #         (n1, n4, n5, n1),  # Fail
    #     ]
    #     s = Solution()
    #     for input1, input2, input3, expected in input_and_expected_outputs:
    #         with self.subTest(input1=input1.val, input2=input2.val, input3=input3.val,
    #                           expected=expected.val):
    #             result = s.solve(input1, input2, input3)
    #             self.assertEqual(result, expected)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
