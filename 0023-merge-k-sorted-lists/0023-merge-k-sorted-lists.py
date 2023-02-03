# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        if lists: dummy.next = lists.pop()
        while lists:
            cur = dummy
            l1 = dummy.next
            l2 = lists.pop()
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                    cur = cur.next
                else:
                    cur.next = l2
                    l2 = l2.next
                    cur = cur.next
            if l1:
                cur.next = l1
            else:
                cur.next = l2
        return dummy.next