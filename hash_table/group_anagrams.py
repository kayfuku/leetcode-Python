# Author: leetcode + kei
# Date: July 18, 2021, September 5, 2022
import unittest
from typing import *
from helper_classes import *
from collections import defaultdict


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            # For lowercase English letters
            count = [0] * 26
            print('count:', count)
            # Count the number of characters in a string using list not Counter
            # so that we can convert it into tuple.
            for c in s:
                print('ord(c):', ord(c))
                count[ord(c) - ord('a')] += 1

            print('tuple(count):', tuple(count))
            # tuple is hashable so we can use it as a key. list is not hashable.
            # If the order of elements in a tuple differ, then the hash of the tuple
            # also differs.
            sig = tuple(count)
            ans[sig].append(s)

        print('ans:', ans)
        return ans.values()


class SolutionNG:
    '''
    TypeError: unhashable type: 'Counter'
    '''

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            count = Counter(s)
            ans[count].append(s)

        return ans.values()


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_outputs = [
            # (input1, input2, expected output) depending on number of arguments
            (["eat", "tea", "tan", "ate", "nat", "bat"], {
             ("tan", "nat"), ("bat", ), ("eat", "tea", "ate")}),
        ]
        s = Solution()
        for input1, expected in input_and_expected_outputs:
            with self.subTest(input1=input1, expected=expected):
                result = s.groupAnagrams(input1)
                group_set = set()
                for r in result:
                    group = tuple(r)
                    group_set.add(group)

                self.assertEqual(group_set, expected)

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
