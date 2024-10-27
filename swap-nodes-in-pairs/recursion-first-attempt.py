# Working Solution

## Can consider implementing iteration

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        else:
            p1 = head
            p2 = head.next

            p1_new = p2.next
            p2.next = p1
            p1.next = self.swapPairs(p1_new)
            return p2


            
## Note to Self: took me approx 20 mins to write
