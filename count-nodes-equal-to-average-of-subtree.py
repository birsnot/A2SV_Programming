# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def helper(root):
            nonlocal ans
            if not root:
                return (0, 0)
            lsum, lcount = helper(root.left)
            rsum, rcount = helper(root.right)
            total = root.val + lsum + rsum
            count = 1 + lcount + rcount
            if total//count == root.val:
                ans += 1
            return (total, count)
        helper(root)
        return ans