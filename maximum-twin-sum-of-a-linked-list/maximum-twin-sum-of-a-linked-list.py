# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = deque()
        fast = slow = head
        ans = 0
        while fast:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        while slow:
            temp = stack.pop() + slow.val
            if temp > ans: ans = temp
            slow = slow.next
        return ans
