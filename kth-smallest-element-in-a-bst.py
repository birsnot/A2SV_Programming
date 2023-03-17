# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], K: int) -> int:
        ans = 0
        k = 0
        found = False
        def helper(root):
            nonlocal k, found, ans
            if found or not root:
                return
            helper(root.left)
            k += 1
            if k == K:
                ans = root.val
                found = True
            helper(root.right)
        helper(root)
        return ans