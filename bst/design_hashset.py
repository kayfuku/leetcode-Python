# Author: leetcode + kei
# Date: May 21, 2022
from typing import *
from helper_classes import *
import numpy as np
import unittest


class MyHashSet:

    def __init__(self):
        self.key_range = 769
        self.bucket_array = [Bucket() for i in range(self.key_range)]
        # self.bucket_array = [Bucket_bst() for i in range(self.key_range)]

    def _hash(self, key) -> int:
        return key % self.key_range

    def add(self, key: int) -> None:
        bucket_idx = self._hash(key)
        self.bucket_array[bucket_idx].insert(key)

    def remove(self, key: int) -> None:
        """
        :type key: int
        :rtype: None
        """
        bucket_idx = self._hash(key)
        self.bucket_array[bucket_idx].delete(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        bucket_idx = self._hash(key)
        return self.bucket_array[bucket_idx].exists(key)


class Bucket:
    '''
    Better for interview
    '''

    def __init__(self):
        # a dummy head
        self.head = ListNode(0)

    def insert(self, newValue):
        # if not existed, add the new element to the head of the list.
        if not self.exists(newValue):
            newNode = ListNode(newValue)
            # before: h -> next node
            # after : h -> newNode -> next node
            # link to the next node.
            newNode.next = self.head.next
            # h -> newNode
            self.head.next = newNode

    def delete(self, value):
        # we need prev node to delete node in the list
        prev = self.head
        node = self.head.next
        # traverse to the last node
        while node is not None:
            if node.val == value:
                # remove the current node
                prev.next = node.next
                return
            prev = node
            node = node.next

    def exists(self, value):
        node = self.head.next
        while node is not None:
            if node.val == value:
                # value existed already, do nothing
                return True
            node = node.next
        return False


class Bucket_bst:
    '''
    Faster, but a bit more complicated
    '''

    def __init__(self):
        self.tree = BSTree()

    def insert(self, value):
        self.tree.root = self.tree.insertIntoBST(self.tree.root, value)

    def delete(self, value):
        self.tree.root = self.tree.deleteNode(self.tree.root, value)

    def exists(self, value):
        return (self.tree.searchBST(self.tree.root, value) is not None)


class BSTree:
    def __init__(self):
        self.root = None

    def searchBST(self, node: TreeNode, val: int) -> TreeNode:
        if node is None or val == node.val:
            return node

        return self.searchBST(node.left, val) if val < node.val \
            else self.searchBST(node.right, val)

    def insertIntoBST(self, node: TreeNode, val: int) -> TreeNode:
        if node is None:
            return TreeNode(val)

        if node.val == val:
            # the val already exists. Do nothing.
            return node

        if node.val < val:
            # insert into the right subtree
            node.right = self.insertIntoBST(node.right, val)
        else:
            # insert into the left subtree
            node.left = self.insertIntoBST(node.left, val)

        return node

    def successor(self, node):
        """
        One step right and then always left
        """
        node = node.right
        while node.left:
            node = node.left
        return node.val

    def predecessor(self, node):
        """
        One step left and then always right
        """
        node = node.left
        while node.right:
            node = node.right
        return node.val

    def deleteNode(self, node: TreeNode, key: int) -> TreeNode:
        if node is None:
            return None

        # delete from the right subtree
        if key > node.val:
            node.right = self.deleteNode(node.right, key)
        # delete from the left subtree
        elif key < node.val:
            node.left = self.deleteNode(node.left, key)
        # delete the current node
        else:
            if node.left is None and node.right is None:
                # the node is a leaf
                node = None
            elif node.right:
                # the node is not a leaf and has a right child
                node.val = self.successor(node)
                node.right = self.deleteNode(node.right, node.val)
            else:
                # the node is not a leaf, has no right child, and has a left child
                node.val = self.predecessor(node)
                node.left = self.deleteNode(node.left, node.val)

        return node

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


class TestCalc(unittest.TestCase):

    def test_solve(self):
        '''
        For more than one argument
        For one argument, comment out some lines.
        '''
        input_and_expected_outputs = [
            # ((input), expected output) or
            # (input, expected output)
            (([0, 1, 2], 3), 6),
            (([0, 1], 3), 5),
        ]
        s = MyHashSet()
        for input, expected in input_and_expected_outputs:
            # result = s.solve(input)
            result = s.solve(*input)
            self.assertEqual(result, expected)


def main():
    """ For testing """
    unittest.main()


if __name__ == '__main__':
    main()
