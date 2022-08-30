from typing_extensions import Self


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None

    def __init__(self, x: int = 0, node: Self = None):
        self.val = x
        self.next = node


class TreeNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.left = None
        self.right = None

    def __init__(self, val: int = 0, left: Self = None, right: Self = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)


class Node:
    def __init__(self, val: int = 0):
        self.val = val
        self.neighbors = []

    def __init__(self, val: int = 0, neighbors: Self = None):
        self.val = val
        self.neighbors = neighbors
