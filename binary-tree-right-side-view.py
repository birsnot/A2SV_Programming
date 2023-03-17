# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        last_d = 0
        ans = []
        def helper(root, d):
            nonlocal last_d
            if not root:
                return
            d += 1
            if d > last_d:
                ans.append(root.val)
                last_d = d
            helper(root.right, d)
            helper(root.left, d)
        helper(root, 0)
        return ans