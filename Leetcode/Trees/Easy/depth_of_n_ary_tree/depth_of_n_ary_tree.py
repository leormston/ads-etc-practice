"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def walk(self, ptr, arr, count):
        if ptr is None:
            return
        arr.append(count)
        for child in ptr.children:
            self.walk(child, arr, count+1)
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        arr = []
        self.walk(root, arr, 1)
        print(arr)
        return max(arr)