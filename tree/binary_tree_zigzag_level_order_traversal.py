# Author: leetcode + kei
# Date: July 21, 2021
from typing import *
from helper_classes import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if root is None:
            return []
        # start with the level 0 with a delimiter
        queue = deque([root, ])
        level = 0

        while queue:
            level_list = deque()
            size = len(queue)
            for i in range(size):
                curr_node = queue.popleft()

                if level % 2 == 0:
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)


            # we finish one level
            ret.append(level_list)
            level += 1

        return ret

def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 8
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
