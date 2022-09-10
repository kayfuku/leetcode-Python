# Author: leetcode + kei
# Date: July 21, 2021, September 10, 2022
import unittest
from typing import *
from helper_classes import *


class Solution1_1:
    '''
    1-1. Recursive
    '''

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        def dfs(node: TreeNode, rem: TreeNode) -> bool:
            if node is None:
                return False

            rem -= node.val
            if node.left is None and node.right is None:
                # Leaf
                return rem == 0

            return dfs(node.left, rem) or dfs(node.right, rem)

        return dfs(root, sum)


class Solution1_2:
    '''
    1-2. Recursive
    '''

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        sum -= root.val
        if root.left is None and root.right is None:
            # 'root' is a leaf node.
            return sum == 0

        return self.hasPathSum(root.left, sum) or \
            self.hasPathSum(root.right, sum)


class Solution2:
    '''
    2. Iterative
    '''

    # TODO: why WA?
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        stack = [(root, sum), ]
        while stack:
            node, curr_sum = stack.pop()
            curr_sum -= node.val
            if node.left is None and node.right is None:
                return curr_sum == 0

            if node.right:
                stack.append((node.right, curr_sum))
            if node.left:
                stack.append((node.left, curr_sum))

        return False


class TestSolution(unittest.TestCase):

    def test_solve(self):
        '''
        Test
        '''
        input_and_expected_outputs = [
            # (input1, input2, expected output) depending on number of arguments
            ([0, 1, 2], 3, 6),
            ([0, 1], 3, 5),
        ]
        s = Solution()
        for input1, input2, expected in input_and_expected_outputs:
            with self.subTest(input1=input1, input2=input2, expected=expected):
                result = s.solve(input1, input2)
                self.assertEqual(result, expected)

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
    #     result = s.solve(n1)
    #     self.assertEqual(result, 4)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
