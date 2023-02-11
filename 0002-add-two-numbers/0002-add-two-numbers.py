# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = n2 = 0
        mul = 1
        while l1:
            n1 += l1.val*mul
            l1 = l1.next
            mul *= 10
        mul = 1
        while l2:
            n2 += l2.val*mul
            l2 = l2.next
            mul *= 10
        ans = str(n1+n2)
        head = ListNode(ans[0])
        for d in ans[1:]: head = ListNode(d, head)
        return head