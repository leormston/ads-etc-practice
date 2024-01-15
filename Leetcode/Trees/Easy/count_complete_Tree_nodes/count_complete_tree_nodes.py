# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def walk(self, ptr, arr):
        if ptr is None:
            return
        self.walk(ptr.left, arr)
        arr.append(ptr.val)
        self.walk(ptr.right, arr)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        arr = []
        self.walk(root, arr)
        return len(arr)