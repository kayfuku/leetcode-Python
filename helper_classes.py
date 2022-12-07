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
    Union Find (Disjoint Set with path compression and union by rank)
    n : int, the number of nodes
    roots : list, list of parents.
        If value is negative, the index is a root node number of a tree/group, and
        the absolute value is the number of nodes in the tree.
    rank : list, height of the tree
    '''

    def __init__(self, n):
        '''
        O(N) time and space
        '''
        self.n = n
        self.roots = [-1] * n
        self.rank = [0] * n
        self.num_of_groups = n

    def find(self, x):
        '''
        Find roots of node x.
        O(logN) or O(α(N)) time, where N is the number of vertices in the graph.
        α refers to the Inverse Ackermann function. In practice, we assume
        it's a constant. In other words, O(α(N)) is regarded as O(1) on average.
        x : int, node number
        '''
        if (self.roots[x] < 0):
            # x is a root node.
            return x
        # Path compression implementation
        # Note that path compression needs recursion stacks of size O(N).
        self.roots[x] = self.find(self.roots[x])
        return self.roots[x]

    def find_without_pc(self, x):
        '''
        Find roots of node x.
        O(logN) time
        x : int, node number
        '''
        if (self.roots[x] < 0):
            # x is a root node.
            return x
        # Without path compression
        return self.find_without_pc(self.roots[x])

    def unite(self, x, y):
        '''
        Unite trees.
        O(logN) or O(α(N)) time
        x : int, node number in one tree
        y : int, node number in another tree
        '''
        root_x = self.find(x)
        root_y = self.find(y)
        if (root_x == root_y):
            return False
        # Merge the lower-rank group into the higher-rank group.
        if (self.rank[root_x] > self.rank[root_y]):
            # Add the number of nodes in tree root_y to tree root_x.
            self.roots[root_x] += self.roots[root_y]
            # Set root_x as a root node of root_y.
            self.roots[root_y] = root_x
        else:
            self.roots[root_y] += self.roots[root_x]
            self.roots[root_x] = root_y
            if (self.rank[root_x] == self.rank[root_y]):
                self.rank[root_y] += 1

        self.num_of_groups -= 1
        return True

    def is_connected(self, x, y):
        '''
        Check if x and y are connected, which means they are in the same tree.
        O(logN) or O(α(N)) time
        x : int, one node number
        y : int, another node number
        '''
        # Return True if their root nodes are the same.
        return self.find(x) == self.find(y)

    def get_tree_size(self, x):
        '''
        Get the tree size.
        O(logN) or O(α(N)) time
        x : int, node number
        '''
        return -self.roots[self.find(x)]

    def get_roots(self):
        '''
        Get a list of the roots.
        O(N) time
        '''
        return [i for i, x in enumerate(self.roots) if x < 0]

    def get_number_of_groups(self):
        '''
        Get the number of trees/groups.
        O(1) time
        '''
        return self.num_of_groups

    def get_all_group_members(self):
        '''
        Get all lists of nodes for all trees/groups.
        O(NlogN) or O(N・α(N)) time
        '''
        # K: root, V: list of nodes
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
