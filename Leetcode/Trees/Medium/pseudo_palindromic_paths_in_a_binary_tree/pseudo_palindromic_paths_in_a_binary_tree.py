# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_leaf(self, ptr, arr, path):
        if ptr.left is None and ptr.right is None:
            arr.append([x for x in path])
            return
        else:
            if ptr.left:
                path.append(ptr.left.val)
                self.find_leaf(ptr.left, arr, path)
                path.pop(-1)
            if ptr.right:
                path.append(ptr.right.val)
                self.find_leaf(ptr.right, arr, path)
                path.pop(-1)
    def check_p(self, arr):
        odd = False
        unique = set(arr)
        if len(unique) == 1:
            return True
        for i in unique:
            if arr.count(i) % 2 != 0 and odd == True:
                return False
            elif arr.count(i) % 2 != 0 and odd ==False:
                odd = True
        return True
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        arr = []
        self.find_leaf(root, arr, [root.val])
        count =0
        seen = []
        n = []
        for a in arr:
            if a in seen:
                count += 1
                continue
            if a in n:
                continue
            p = self.check_p(sorted(a))
            if p:
                seen.append(a)
                count += 1
            else:
                n.append(a)
        return count
        