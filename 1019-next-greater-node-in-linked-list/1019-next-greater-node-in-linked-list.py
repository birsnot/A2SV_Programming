# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        cur = head
        i = 0
        while cur:
            cur.val = (cur.val, i)
            cur = cur.next
            i += 1
        ans = [0]*i
        cur = dummy = ListNode(0, head)
        prev = None
        while cur.next.next:
            val = cur.next.next.val[0]
            if cur.next.val[0] < val:
                ans[cur.next.val[1]] = val
                cur.next = cur.next.next
                while prev and prev.val[0] < val:
                    ans[prev.val[1]] = val
                    prev = prev.next
            else:
                temp = cur.next
                cur.next = cur.next.next
                temp.next = prev
                prev = temp
        return ans