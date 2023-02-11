# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode(0, head)
        ans = ListNode()
        while cur.next:
            val = cur.next.val
            node = cur.next
            cur.next = cur.next.next
            ptr = ans
            while ptr.next and ptr.next.val < val:
                ptr = ptr.next
            if ptr.next:
                node.next = ptr.next
                ptr.next = node
            else:
                node.next = None
                ptr.next = node
        return ans.next