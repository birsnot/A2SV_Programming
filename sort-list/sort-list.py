# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeSort(hd):
            if not hd.next: return hd
            slow = hd
            fast = slow.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            half2 = mergeSort(slow.next)
            slow.next = None
            half1 = mergeSort(hd)
            cur = dummy = ListNode()
            while half1 and half2:
                if half1.val < half2.val:
                    cur.next = half1
                    half1 = half1.next
                else:
                    cur.next = half2
                    half2 = half2.next
                cur = cur.next
            cur.next = half1 or half2
            return dummy.next
        if not head: return head
        return mergeSort(head)
