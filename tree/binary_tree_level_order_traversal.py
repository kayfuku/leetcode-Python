# Author: leetcode + kei
# Date: July 21, 2021
from typing import *
from helper_classes import *


from collections import deque


class Solution:
    def levelOrder(self, root):
        """
        1. BFS
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels

        level = 0
        queue = deque([root, ])
        while queue:
            # start the current level
            list_level = []
            # number of elements in the current level
            size = len(queue)

            for i in range(size):
                node = queue.popleft()
                # fulfill the current level
                list_level.append(node.val)

                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            levels.append(list_level)

            # go to next level
            level += 1

        return levels


class Solution:
    def levelOrder(self, root):
        """
        DFS, recursive, not recommended for interview
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels

        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 8
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
