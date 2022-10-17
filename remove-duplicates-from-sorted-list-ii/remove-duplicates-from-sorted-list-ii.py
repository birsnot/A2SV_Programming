# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        first = True
        head = p3 = None
        while p1:
            dup = False
            p2 = p1
            v = p1.val
            while p1.next and v == p1.next.val:
                p1 = p1.next
                dup = True
            p1 = p1.next
            if not dup:
                if first:
                    head = p3 = p2
                    first = False
                else:
                    p3.next = p2
                    p3 = p2
        if p3:
            p3.next = None
        return head
