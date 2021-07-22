# Author: leetcode + kei
# Date: July 21, 2021
from typing import *
from helper_classes import *


class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        O(N) time and space
        """
        def helper(left, right):
            if left > right:
                return None

            # always choose left middle node as a root
            mid = (left + right) // 2

            # preorder traversal: node -> left -> right
            node = TreeNode(nums[mid])
            node.left = helper(left, mid - 1)
            node.right = helper(mid + 1, right)
            return node

        return helper(0, len(nums) - 1)

def main():
    """ For testing """
    s = Solution()

    # Test args
    # nums = [3, 2, 5, 1]
    # target = 8
    # print(s.solve(nums, target))


if __name__ == '__main__':
    main()
