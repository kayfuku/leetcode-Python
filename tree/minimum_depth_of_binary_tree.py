# Author: leetcode + kei
# Date: July 21, 2021
from typing import *
from helper_classes import *


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        children = [root.left, root.right]
        # if we're at leaf node
        if root.left is None and root.right is None:
            return 1

        # the node has one or more child nodes.
        min_depth = float('inf')
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)

        return min_depth + 1

def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 8
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
