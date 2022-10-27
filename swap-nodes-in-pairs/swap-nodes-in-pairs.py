# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        p = dummy
        while p.next and p.next.next:
            temp1, temp2 = p.next, p.next.next.next
            p.next = p.next.next
            p = p.next.next = temp1
            p.next = temp2
        return dummy.next
