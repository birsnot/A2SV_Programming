# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        len_ = 0
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
            len_ += 1
        k %= len_
        end = prev
        cur = prev.next
        k -= 1
        for _ in range(k):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        head = prev
        if k == -1:
            prev = end
        else:
            prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        if k == -1:
            end.next = None
            return prev
        else:
            end.next = prev
            return head