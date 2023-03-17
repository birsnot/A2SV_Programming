# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        max_ = 0
        ans = []
        last = [0.5, 0]

        def helper(root):
            nonlocal last, max_, ans
            if not root:
                return
            helper(root.left)
            if last[0] == root.val:
                last[1] += 1
            else:
                last = [root.val, 1]
            if last[1] > max_:
                max_ = last[1]
                ans = [root.val]
            elif last[1] == max_:
                ans.append(root.val)
            helper(root.right)
        
        helper(root)
        return ans