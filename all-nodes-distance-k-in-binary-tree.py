# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k >= 500: return []
        if k == 0: return [target.val]
        ans = []
        def below(node, k):
            if k == 0:
                ans.append(node.val)
                return
            if node.left:
                below(node.left, k - 1)
            if node.right:
                below(node.right, k - 1)
        def dfs(node):
            if node.val == target.val:
                below(node, k)
                return 1
            cur = cur2 = 0
            if node.left:
                cur = dfs(node.left)
                if 0 < cur < k and node.right:
                    below(node.right, k - cur - 1)
                elif cur == k:
                    ans.append(node.val)
            if node.right:
                cur2 = dfs(node.right)
                if 0 < cur2 < k and node.left:
                    below(node.left, k - cur2 - 1)
                elif cur2 == k:
                    ans.append(node.val)
            cur = max(cur, cur2)
            return cur + (cur > 0)
        dfs(root)
        return ans