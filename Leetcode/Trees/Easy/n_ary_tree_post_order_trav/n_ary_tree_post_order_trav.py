"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def walk(self, ptr, arr):
        if ptr is None:
            return
        
        for child in ptr.children:
            self.walk(child, arr)
        arr.append(ptr.val)
    def postorder(self, root: 'Node') -> List[int]:
        arr = []
        self.walk(root, arr)
        return arr