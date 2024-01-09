# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchPre(self, root, arr):
        if root == None:
            arr.append(None)
            return

        arr.append(root.val)
        self.searchPre(root.left, arr)
        self.searchPre(root.right, arr)

    def searchPost(self, root, arr):
        if root == None:
            arr.append(None)
            return
        
        self.searchPost(root.left, arr)
        self.searchPost(root.right, arr)
        arr.append(root.val)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        pre_left = []
        self.searchPre(root.left, pre_left)
        post_right = []
        self.searchPost(root.right, post_right)

        return pre_left[::-1] == post_right