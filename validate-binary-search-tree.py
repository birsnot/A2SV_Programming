# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nums = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            nums.append(root.val)
            helper(root.right)
        helper(root)
        N = len(nums) - 1
        for i in range(N):
            if nums[i] >= nums[i+1]:
                return False
        return True