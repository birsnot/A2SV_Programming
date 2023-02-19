# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack1 = [root]
        stack2 = []
        ans = []
        while stack1:
            temp = []
            while stack1:
                node = stack1.pop()
                if node:
                    temp.append(node.val)
                    stack2.append(node.left)
                    stack2.append(node.right)
            if temp: ans.append(temp)
            temp = []
            while stack2:
                node = stack2.pop()
                if node:
                    temp.append(node.val)
                    stack1.append(node.right)
                    stack1.append(node.left)
            if temp: ans.append(temp)
        return ans