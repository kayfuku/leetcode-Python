# Author: leetcode + kei
# Date: May 28, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest

import collections


class Solution:
    def __init__(self):
        pass

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # Create a hash value
        def get_hash(string: str):
            key = []
            for i in range(1, len(string)):
                # Why modulo 26?
                diff = (ord(string[i]) - ord(string[i - 1])) % 26
                c = chr(diff + ord('a'))
                key.append(c)
            return ''.join(key)

        # Create a hash value (hash_key) for each string and append the string
        # to the list of hash values i.e. mapHashToList["cd"] = ["acf", "gil", "xzc"]
        groups = collections.defaultdict(list)
        for string in strings:
            hash_key = get_hash(string)
            groups[hash_key].append(string)

        # Return a list of all of the grouped strings
        return list(groups.values())


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
