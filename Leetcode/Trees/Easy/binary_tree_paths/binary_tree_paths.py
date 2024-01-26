# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_path(self, ptr, path, arr):
        if ptr.left is None and ptr.right is None:
            arr.append([str(x) for x in path])
            return
        else:
            if ptr.left is not None:
                path.append(ptr.left.val)
                self.find_path(ptr.left, path, arr)
                path.pop(-1)
            
            if ptr.right is not None:
                path.append(ptr.right.val)
                self.find_path(ptr.right, path, arr)
                path.pop(-1)
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        arr =  []
        self.find_path(root, [root.val], arr)
        return ["->".join(path) for path in arr]