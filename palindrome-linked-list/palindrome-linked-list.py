# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        sz = 0
        p = head
        while p:
            p = p.next
            sz += 1
        if sz < 2:
            return True
        half = sz//2
        curr = head
        prev = None
        while half:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
            half -= 1
        if sz%2==1:
            curr = curr.next
        while curr and prev:
            if curr.val != prev.val:
                return False
            curr = curr.next
            prev = prev.next
        return True
