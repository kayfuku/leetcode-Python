from collections import defaultdict
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


class UnionFind(object):
    '''
    Union Find
    n : int, the number of nodes
    roots : list, list of parents.
        If value is negative, the index is a root node number of a tree/group, and
        the absolute value is the number of nodes in the tree.
    rank : list, height of the tree
    '''

    def __init__(self, n):
        self.n = n
        self.roots = [-1] * (n + 1)
        self.rank = [0] * (n + 1)

    def find(self, x):
        '''
        Find roots of node x.
        x : int, node number
        '''
        if (self.roots[x] < 0):
            # x is a root node.
            return x
        parent = self.roots[x]
        return self.find(parent)

    def unite(self, x, y):
        '''
        Unite trees.
        x : int, node number in one tree
        y : int, node number in another tree
        '''
        x = self.find(x)
        y = self.find(y)
        if (x == y):
            return
        # Merge the lower-rank group into the higher-rank group.
        if (self.rank[x] > self.rank[y]):
            # Add the number of nodes in tree y to tree x.
            self.roots[x] += self.roots[y]
            # Set x as a root node of y.
            self.roots[y] = x
        elif self.rank[x] < self.rank[y]:
            self.roots[y] += self.roots[x]
            self.roots[x] = y
            if (self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def is_connected(self, x, y):
        '''
        Check if x and y are connected, which means they are in the same tree.
        x : int, one node number
        y : int, another node number
        '''
        # Return True if their root nodes are the same.
        return self.find(x) == self.find(y)

    def get_tree_size(self, x):
        '''
        Get the tree size.
        x : int, node number
        '''
        return -self.roots[self.find(x)]

    def get_roots(self):
        '''
        Get a list of the roots.
        '''
        return [i for i, x in enumerate(self.roots) if x < 0]

    def get_number_of_group(self):
        '''
        Get the number of trees/groups.
        '''
        return len(self.get_roots())

    def get_all_group_members(self):
        '''
        Get all lists of nodes for all trees/groups.
        '''
        # K: root, V: list of nodes
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
