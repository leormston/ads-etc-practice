# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def walk(self, ptr, arr, val):
        if ptr is None:
            return
        if ptr.val == val:
            arr.append(ptr)
            return
        self.walk(ptr.left, arr, val)
        self.walk(ptr.right, arr, val)

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        arr =[ ]
        self.walk(root, arr, val )
        if arr == []:
            return None
        else:
            return arr[0]
        