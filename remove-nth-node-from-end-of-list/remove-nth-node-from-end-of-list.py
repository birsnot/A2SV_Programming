# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            count += 1
        sz = count<<1
        if fast:
            sz += 1
        m = sz - n
        if m > count:
            m -= count + 1
            for _ in range(m):
                slow = slow.next
            slow.next = slow.next.next
            return head
        else:
            ans = dummy = ListNode(0,head)
            for _ in range(m):
                dummy = dummy.next
            dummy.next = dummy.next.next
            return ans.next
