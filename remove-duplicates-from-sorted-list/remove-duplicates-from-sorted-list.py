# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        p1 = p2 = head
        while p1.next:
            p1 = p1.next
            if p2.val != p1.val:
                p2.next = p1
                p2 = p2.next
        p2.next = None
        return head
