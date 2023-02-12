# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        odd_head = odd = ListNode()
        even_head = even = ListNode()
        while head:
            odd.next = head
            odd = odd.next
            head = head.next
            if head:
                even.next = head
                even = even.next
                head = head.next
        even.next = None
        odd.next = even_head.next
        return odd_head.next