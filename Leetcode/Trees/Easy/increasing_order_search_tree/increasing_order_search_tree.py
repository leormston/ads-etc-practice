# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getTree(self, ptr, arr) -> None:
        if ptr is None:
            return
        self.getTree(ptr.left, arr)
        arr.append(ptr.val)
        self.getTree(ptr.right, arr)
    
    def makeTree(self, arr) -> TreeNode:
        head = TreeNode(arr[0])
        ptr = head
        for node in arr[1:]:
            ptr.right = TreeNode(node)
            ptr = ptr.right
        return head
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr = []
        self.getTree(root, arr)
        return self.makeTree(arr)