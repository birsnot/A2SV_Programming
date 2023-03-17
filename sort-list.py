# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeSort(head):
            if not head or not head.next:
                return head
            slow = head
            fast = head.next
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            right = mergeSort(slow.next)
            slow.next = None
            left = mergeSort(head)
            cur = dummy = ListNode()
            while left and right:
                if left.val < right.val:
                    cur.next = left
                    left = left.next
                else:
                    cur.next = right
                    right = right.next
                cur = cur.next
            if left: cur.next = left
            if right: cur.next = right
            return dummy.next
        return mergeSort(head)