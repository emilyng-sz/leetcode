# Working solution

## This is O(n) time solution but also O(n) space

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        
        # create a list
        length = 0
        while head is not None:
            stack.append(head.val)
            head = head.next
            length += 1
        
        # use O(1) list indexing
        for i in range(length//2):
            if stack[i] != stack[length-i-1]:
                return False

        return True

## Notes:
# This version has the fastest time and second lowest space for all approaches
# improve time even more by using stack == stack[::-1]      
