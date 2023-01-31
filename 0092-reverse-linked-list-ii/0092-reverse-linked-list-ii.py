# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        first = dummy = ListNode(0, head)
        left_ = left - 1
        for _ in range(left_):
            first = first.next
        end = prev = first.next
        cur = prev.next
        rev_len = right-left
        for _ in range(rev_len):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        first.next = prev
        end.next = cur
        return dummy.next