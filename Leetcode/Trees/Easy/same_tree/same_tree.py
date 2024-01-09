# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def search(self, ptr, arr):
        if ptr is None:
            arr.append(None)
            return
        arr.append(ptr.val)
        self.search(ptr.left, arr)
        self.search(ptr.right, arr)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr_one = []
        arr_two = []
        self.search(p, arr_one)
        self.search(q, arr_two)
        return arr_one == arr_two