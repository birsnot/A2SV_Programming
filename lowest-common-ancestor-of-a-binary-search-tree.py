# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root):
            if root.val < p.val and root.val < q.val:
                return helper(root.right)
            elif root.val > p.val and root.val > q.val:
                return helper(root.left)
            return root
        return helper(root)