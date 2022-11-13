# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        half2 = slow.next
        prev = slow.next = None
        while half2:
            temp = half2.next
            half2.next = prev
            prev = half2
            half2 = temp
        cur = head
        left = head.next
        right = prev
        while left and right:
            temp = right
            right = right.next
            cur.next = temp
            cur = cur.next
            temp = left
            left = left.next
            cur.next = temp
            cur = cur.next
