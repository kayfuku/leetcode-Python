# Author: leetcode + kei
# Date: July 21, 2021
from typing import *
from helper_classes import *


class Solution:

    def validate(self, node, low=None, high=None):
        # Empty trees are valid BSTs.
        if node is None:
            return True
        # The current node's value must be between low and high.
        if low is not None and node.val <= low:
            return False
        if high is not None and node.val >= high:
            return False

        # The left and right subtree must also be valid.
        return (self.validate(node.left, low, node.val) and
                self.validate(node.right, node.val, high))

    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root)


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 8
    # print(s.solve(nums, target))
    print(math.inf)


if __name__ == '__main__':
    main()
