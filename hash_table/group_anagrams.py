# Author: leetcode + kei
# Date: July 18, 2021
from typing import *
from helper_classes import *
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            print('count:', count)
            for c in s:
                print('ord(c):', ord(c))
                count[ord(c) - ord('a')] += 1

            print('tuple(count):', tuple(count))
            # tuple is hashable so we can use it as a key. list is not hashable.
            ans[tuple(count)].append(s)

        print('ans:', ans)
        return ans.values()


def main():
    """ For testing """
    s = Solution()

    # Test args
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s.groupAnagrams(strs))


if __name__ == '__main__':
    main()
