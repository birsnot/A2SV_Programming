# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = slow = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        max_ = 0
        while prev:
            sum_ = prev.val + slow.val
            if sum_ > max_: max_ = sum_
            prev, slow = prev.next, slow.next
        return max_