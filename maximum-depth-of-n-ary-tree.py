"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def helper(root):
            if not root: return 0
            mx = 0
            for ch in root.children:
                mx = max(mx, helper(ch))
            return mx + 1
        return helper(root)