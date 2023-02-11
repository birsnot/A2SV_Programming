# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        while head and head.next:
            if head.val == head.next.val:
                val = head.val
                head = head.next.next
                while head and head.val == val:
                    head = head.next
            else:
                cur.next = head
                cur = cur.next
                head = head.next
        cur.next = head
        return dummy.next