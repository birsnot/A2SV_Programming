# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = {0: 1}
        ans = 0
        def helper(root, sum_):
            if not root: return
            nonlocal ans
            sum_ += root.val
            ans += sums.get(sum_ - k, 0)
            sums[sum_] = sums.get(sum_, 0) + 1
            helper(root.left, sum_)
            helper(root.right, sum_)
            sums[sum_] -= 1
        helper(root, 0)
        return ans