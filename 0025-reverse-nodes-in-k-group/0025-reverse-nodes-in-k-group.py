# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: return head
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next
        rvrs = size//k
        prev_end = dummy = ListNode()
        cur = head
        for _ in range(rvrs):
            end = cur
            prev = None
            for __ in range(k):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            prev_end.next = prev
            prev_end = end
        end.next = cur
        return dummy.next