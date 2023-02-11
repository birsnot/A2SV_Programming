# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = p = ListNode(0)
        carry = 0
        while l1 and l2:
            n = l1.val + l2.val + carry
            p.next = ListNode(n%10)
            p, l1, l2 = p.next, l1.next, l2.next
            carry = n//10
        while l1:
            n = l1.val + carry
            p.next = ListNode(n%10)
            p, l1 = p.next, l1.next
            carry = n//10
        while l2:
            n = l2.val + carry
            p.next = ListNode(n%10)
            p, l2 = p.next, l2.next
            carry = n//10
        if carry:
            p.next = ListNode(carry)
        return ans.next