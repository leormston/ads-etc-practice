# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def walk(self, root, arr, low, high) -> int:
        if root == None:
            return 0
        if root.val >= low and root.val <= high:
            arr.append(root.val)
        
        self.walk(root.left, arr ,low, high)
        self.walk(root.right, arr, low, high)
        
        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        arr = []
        self.walk(root, arr, low, high)
        return sum(arr)