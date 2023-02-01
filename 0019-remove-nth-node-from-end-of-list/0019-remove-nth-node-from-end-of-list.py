# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        lead = head
        for _ in range(n):
            lead = lead.next
        cur = dummy
        while lead:
            cur = cur.next
            lead = lead.next
        cur.next = cur.next.next
        return dummy.next