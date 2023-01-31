# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        left = prev
        if fast:
            right = slow.next
        else:
            right = slow
        while left and right and left.val == right.val:
            left = left.next
            right = right.next
        if left or right:
            return False
        return True