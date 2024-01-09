# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def find_leaves(self, ptr, arr):
        if ptr == None:
            return
        if ptr.left == None and ptr.right == None:
            arr.append(ptr.val)
            return
        self.find_leaves(ptr.left, arr)
        self.find_leaves(ptr.right, arr)
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_array_one = []
        self.find_leaves(root1, leaf_array_one)
        leaf_array_two = []
        self.find_leaves(root2, leaf_array_two)
        return leaf_array_one == leaf_array_two
        