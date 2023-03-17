# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(l, r):
            if not l or not r: return l == r
            if l.val != r.val: return False
            return helper(r.left, l.right) and helper(l.left, r.right)
        return helper(root.left, root.right)