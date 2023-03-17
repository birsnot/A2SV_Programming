# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def helper(ans, path, root):
            if not root: return
            if not root.left and not root.right:
                path.append(str(root.val))
                ans.append("->".join(path))
                path.pop()
                return
            path.append(str(root.val))
            helper(ans, path, root.left)
            helper(ans, path, root.right)
            path.pop()
            return
        ans = []
        helper(ans, [], root)
        return ans