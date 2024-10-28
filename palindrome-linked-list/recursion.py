# Working Solution - referenced from an online solution

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.curr = head  # helps to store the very original node towards the very end of the LL
        return self.solve(head) 

    def solve(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        
        ans = (self.solve(head.next) and head.val == self.curr.val)
        # returns True, when LL at end of list, then head.val becomes Last Node, compared to First Node
        self.curr = self.curr.next
        
        return ans