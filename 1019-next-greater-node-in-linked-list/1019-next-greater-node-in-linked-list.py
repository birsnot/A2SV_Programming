# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        ans = [0]*len(nums)
        monostack = []
        for i, n in enumerate(nums):
            while monostack and nums[monostack[-1]] < n:
                ans[monostack.pop()] = n
            monostack.append(i)
        return ans