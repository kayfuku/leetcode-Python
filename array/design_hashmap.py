# Author: leetcode + kei
# Date: May 22, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest


class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # better to be a prime number, less collision
        self.key_space = 2069
        self.bucket_array = [Bucket() for i in range(self.key_space)]

    def _hash(self, key) -> int:
        return key % self.key_space

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        bucket_idx = self._hash(key)
        self.bucket_array[bucket_idx].put(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        bucket_idx = self._hash(key)
        return self.bucket_array[bucket_idx].get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        bucket_idx = self._hash(key)
        self.bucket_array[bucket_idx].remove(key)


class Bucket:
    def __init__(self):
        # (k, v) is put in the list
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def put(self, key, value):
        for i, (k, v) in enumerate(self.bucket):
            if k == key:
                self.bucket[i] = (key, value)
                return
        self.bucket.append((key, value))

    def remove(self, key):
        for i, (k, v) in enumerate(self.bucket):
            if k == key:
                del self.bucket[i]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        For more than one argument
        For one argument, comment out some lines.
        '''
        input_and_expected_outputs = [
            # ((input), expected output) or
            # (input, expected output) depending on number of arguments
            (([0, 1, 2], 3), 6),
            (([0, 1], 3), 5),
        ]
        s = Solution()
        for input, expected in input_and_expected_outputs:
            # result = s.solve(input)
            result = s.solve(*input)
            self.assertEqual(result, expected)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
