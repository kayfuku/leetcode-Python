# Author: leetcode + kei
# Date: May ?, 2022
from typing import *
from helper_classes import *
import numpy as np


class Solution:

    def __init__(self):
        pass

    def lowest_common_ancestor(
            self, root: TreeNode, p: int, q: int) -> TreeNode:
        def recurse_tree(curr_node):
            if not curr_node or curr_node.val == p or curr_node.val == q:
                # No need to further explore this branch because
                # if the node is p or q, then the node can be the LCA even if there is
                # the other node in this brach.
                return curr_node

            left = recurse_tree(curr_node.left)
            right = recurse_tree(curr_node.right)

            if left and right:
                # Return the node when both child nodes are not null.
                return curr_node

            # Return not-null child node, and
            # return null if both nodes are null.
            return left if left else right

        lca = recurse_tree(root)

        return lca

    def getDirections(
            self, root: Optional[TreeNode],
            start_value: int, dest_value: int) -> str:
        ancestor = self.lowest_common_ancestor(root, start_value, dest_value)

        def get_direction(node: TreeNode, value: int, steps: List[str]):
            if not node:
                return False
            if node.val == value:
                return True
            steps.append('L')
            if get_direction(node.left, value, steps):
                return True
            steps.pop()
            steps.append('R')
            if get_direction(node.right, value, steps):
                return True
            steps.pop()
            return False

        to_start = []
        get_direction(ancestor, start_value, to_start)
        to_dest = []
        get_direction(ancestor, dest_value, to_dest)

        direction = []
        for _ in range(len(to_start)):
            direction.append('U')
        for d in to_dest:
            direction.append(d)

        return ''.join(direction)


def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 2
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
