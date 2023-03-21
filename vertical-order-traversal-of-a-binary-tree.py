# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        stk = deque([(root, 0)])
        ans = deque()
        left = 0
        right = -1
        while stk:
            cols = defaultdict(list)
            n = len(stk)
            for _ in range(n):
                node, c = stk.popleft()
                cols[c].append(node.val)
                if node.left:
                    stk.append((node.left, c - 1))
                if node.right:
                    stk.append((node.right, c + 1))
            for c in cols:
                if c < 0:
                    if c < left:
                        left = c
                        ans.appendleft(sorted(cols[c]))
                    else:
                        ans[c - left].extend(sorted(cols[c]))
                else:
                    if c > right:
                        right = c
                        ans.append(sorted(cols[c]))
                    else:
                        ans[c - left].extend(sorted(cols[c]))
        return ans