# Author: leetcode + kei
# Date: May 8, 2022, November 23 2022
import unittest
from typing import *
from helper_classes import *
import numpy as np


class Solution:

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


class Review:
    '''
    5
    |\
    1 2
    | |\
    2 6 4
    '''

    def getDirections(
            self, root: Optional[TreeNode],
            startValue: int, destValue: int) -> str:

        def get_lowest_common_ancestor(node, s, t):
            if node is None:
                return None
            if node.val == s or node.val == t:
                return node

            left = get_lowest_common_ancestor(node.left, s, t)
            right = get_lowest_common_ancestor(node.right, s, t)
            # Don't use 'not'! It's confusing.
            if left and right:
                return node

            # Don't use 'not'! It's confusing.
            return left if left else right

        def get_direction(node: TreeNode, x: int, steps: List[str]):
            if node is None:
                return False

            if node.val == x:
                return True

            if get_direction(node.left, x, steps):
                steps.append('L')
                return True

            if get_direction(node.right, x, steps):
                steps.append('R')
                return True

            return False

        def reverse(li):
            i = 0
            j = len(li) - 1
            while i < j:
                li[i], li[j] = li[j], li[i]
                i += 1
                j -= 1

        lca = get_lowest_common_ancestor(root, startValue, destValue)
        to_start = []
        get_direction(lca, startValue, to_start)
        to_dest = []
        get_direction(lca, destValue, to_dest)

        steps = []
        for _ in to_start:
            steps.append('U')
        # NG! Reversing and Reverse sorting are **NOT** equal!
        # to_dest = sorted(to_dest, reverse=True)
        reverse(to_dest)
        for d in to_dest:
            steps.append(d)

        return ''.join(steps)


class Cbot:
    '''
    RE
    Author: + kei
    '''

    def getDirections(self, root, startValue, destValue):
        if root is None:
            return None

        # create an empty queue
        q = []

        # create a map to store the parent of each node
        parent = {}

        # add the root node to the queue
        q.append(root)

        # loop until the queue is empty
        while len(q) > 0:
            # get the first element from the queue
            node = q.pop(0)

            # if the current node is start node, break the loop
            if node.val == startValue:
                break

            # add the left and right children of the current node to the queue
            if node.left is not None:
                q.append(node.left)
                parent[node.left.val] = node
            if node.right is not None:
                q.append(node.right)
                parent[node.right.val] = node

        # create a string to store the path
        path = []

        # loop until we reach the destValue
        while destValue != startValue:
            # add the current node to the path
            path.append('U')

            # get the parent of the current node
            pnode = parent[destValue]

            # if the parent's left child has the current value, add 'L' to the path
            if pnode.left is not None and pnode.left.val == destValue:
                path.append('L')
            # else add 'R' to the path
            else:
                path.append('R')

            # update the current value to the parent value
            destValue = pnode.val

        # reverse the path
        path = path[::-1]

        # convert the list to a string
        path = ''.join(path)

        return path


class TestSolution(unittest.TestCase):

    # def test_solve(self):
    #     '''
    #     Test
    #     '''
    #     input_and_expected_outputs = [
    #         # (input1, input2, expected output) depending on number of arguments
    #         ([0, 1, 2], 3, 6),
    #         ([0, 1], 3, 5),
    #     ]
    #     s = Solution()
    #     for input1, input2, expected in input_and_expected_outputs:
    #         with self.subTest(input1=input1, input2=input2, expected=expected):
    #             result = s.solve(input1, input2)
    #             self.assertEqual(result, expected)

    def test_tree(self):
        '''
        Tree test example
              6
             /  \
            2    12
           / \   / \
          1   4 9  14
        '''
        n1 = TreeNode(6)
        n2 = TreeNode(2)
        n3 = TreeNode(12)
        n4 = TreeNode(1)
        n5 = TreeNode(4)
        n6 = TreeNode(9)
        n7 = TreeNode(14)

        n1.left = n2
        n1.right = n3
        n2.left = n4
        n2.right = n5
        n3.left = n6
        n3.right = n7

        input_and_expected_outputs = [
            # (input1, input2, expected output) depending on number of arguments
            (n1, 4, 9, 'UURL'),
            (n1, 2, 4, 'R'),
        ]
        s = Review()
        for input1, input2, input3, expected in input_and_expected_outputs:
            with self.subTest(input1=input1, input2=input2, input3=input3, expected=expected):
                result = s.getDirections(input1, input2, input3)
                self.assertEqual(result, expected)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
