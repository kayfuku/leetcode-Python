# Author: leetcode + kei
# Date: May 9, 2022
from typing import *
from helper_classes import *
import numpy as np


class Solution:

    def __init__(self):
        pass

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Recursive
        '''

        def dfs(node, pre_order):
            if not node:
                return None

            pre_order.append(node.val)
            dfs(node.left, pre_order)
            dfs(node.right, pre_order)

        ret = []
        dfs(root, ret)
        return ret


class Solution2:

    def __init__(self):
        pass

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Iterative
        '''
        ret = []
        if not root:
            return ret

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            ret.append(node.val)

            # Add all the children of the node to stack.
            # Note that right child is first, then left for pre-order traversal.
            # When popped, left child first.
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return ret


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 2
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
