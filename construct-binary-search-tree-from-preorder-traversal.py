# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, pre: List[int]) -> Optional[TreeNode]:
        stk = [TreeNode(1001)]
        for n in pre:
            node = TreeNode(n)
            if stk[-1].val > n: stk[-1].left = node
            else:
                while stk[-1].val < n: root = stk.pop()
                root.right = node
            stk.append(node)
        return stk[0].left