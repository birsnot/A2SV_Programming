# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for i, node in enumerate(lists):
            if node:
                heappush(pq, (node.val, i))
        cur = dummy = ListNode()
        while pq:
            val, i = heappop(pq)
            cur.next = lists[i]
            cur = cur.next
            if lists[i].next:
                lists[i] = lists[i].next
                heappush(pq, (lists[i].val, i))
        return dummy.next