
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __init__(self, x=0, node=None):
        self.val = x
        self.next = node


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)


class Node:
    def __init__(self, val=0):
        self.val = val
        self.neighbors = []

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors
