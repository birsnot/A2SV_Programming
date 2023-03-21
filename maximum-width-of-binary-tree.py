# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stk = deque([(root, 1)])
        ans = 0
        while stk:
            n = len(stk)
            cur = stk[-1][1]- stk[0][1] + 1
            if cur > ans: ans = cur
            for _ in range(n):
                node, i = stk.popleft()
                if node.left:
                    stk.append((node.left, i*2))
                if node.right:
                    stk.append((node.right, i*2 + 1))
        return ans