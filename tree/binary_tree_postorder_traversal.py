# Author: leetcode + kei
# Date: May 10, 2022
from typing import *
from helper_classes import *
import numpy as np


class Solution:
    def __init__(self):
        pass

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Recursive
        '''

        def dfs(node, postorder):
            if not node:
                return None

            dfs(node.left, postorder)
            dfs(node.right, postorder)
            postorder.append(node.val)

        ret = []
        dfs(root, ret)
        return ret


class Solution2:

    def __init__(self):
        pass

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Iterative
        Postorder is actually reversed Right-first-preorder.
        '''
        ret = []
        if not root:
            return ret

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            ret.insert(0, node.val)

            # Right-first-preorder.
            # Push left first so that you can pop right first.
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

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
