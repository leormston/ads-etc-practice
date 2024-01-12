# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_min(self, ptr, depth, arr):
        if ptr.left is None and ptr.right is None:
            arr.append(depth + 1)
            return
        if ptr.left:
            self.find_min(ptr.left, depth+1, arr)
        if ptr.right:
            self.find_min(ptr.right, depth+1, arr)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        arr = []
        self.find_min(root, 0, arr)
        print(arr)

        m = min(arr)
        return m