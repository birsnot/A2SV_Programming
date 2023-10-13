# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def helper(root):
            nonlocal ans
            if ans: return (True, True)
            if not root: return (False, False)
            p_found = q_found = False
            if root.val == p.val:
                p_found = True
            elif root.val == q.val:
                q_found = True
            p_temp, q_temp = helper(root.left)
            p_found |= p_temp
            q_found |= q_temp
            p_temp, q_temp = helper(root.right)
            p_found |= p_temp
            q_found |= q_temp
            if not ans and p_found and q_found:
                ans = root
            return (p_found, q_found)
        helper(root)
        return ans