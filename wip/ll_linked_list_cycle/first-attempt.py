# Working Solution. Took me 4 minutes to write

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        h = set()
        while head is not None:
            if head not in h:
                h.add(head)
            else:
                return True
            head = head.next
        return False  