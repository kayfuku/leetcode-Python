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


class UF:

    def __init__(self, n) -> None:
        self.roots = [i for i in range(n)]

    def find(self, x):
        if self.roots[x] == x:
            # This is the root node.
            return self.roots[x]
        # Keep searching for parent of parent
        return self.find(self.roots[x])

    def unite(self, x, y):
        self.roots[x] = y
