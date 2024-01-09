# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def go_deeper(self, ptr, count):
        if ptr is None:
            return count
        return max(self.go_deeper(ptr.left, count + 1), self.go_deeper(ptr.right, count + 1))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.go_deeper(root, 0)