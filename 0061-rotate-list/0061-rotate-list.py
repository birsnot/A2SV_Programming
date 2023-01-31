# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        len_ = 0
        cur = head
        while cur.next:
            cur = cur.next
            len_ += 1
        turn = cur
        len_ += 1
        k = k%len_
        if not k: return head
        cur = head
        first_len = len_ - k - 1
        for _ in range(first_len):
            cur = cur.next
        ans = cur.next
        cur.next = None
        turn.next = head
        return ans