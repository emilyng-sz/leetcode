# Working Solution - referenced from an online solution

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverse(self, head: ListNode) -> ListNode:
        '''
        use three pointers to reverse LL (prev, curr, next_temp)
        '''
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        slow and fast pointer algo, because slow = mid-point when fast is None
        Then reverse second half of LL
        Then while reversed is not None, compare reversed and first half nodes
        '''
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev = self.reverse(slow)
        while rev:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next
        return True