## This is not a working solution. 
## Added on 26/10/2024 as one of my first few revisions on leetcode content.

## The pointer and looping logic does not work.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # idea is to add each val and also carry the 10 modulo 
        
        # create linkedlist
        l = ListNode()
        l1_pointer = l1
        l2_pointer = l2
        l_pointer = l
        remainder = 0
        while l1_pointer is not None and l2_pointer is not None:
            s = l1_pointer.val + l2_pointer.val + remainder
            print(s)
            l_pointer.val = (s%10) # could be 0 
            remainder = s // 10 # could be 0 
            l1_pointer = l1_pointer.next
            print(l1_pointer.val)
            l2_pointer = l2_pointer.next
            print(l2_pointer.val)
            l_pointer = l_pointer.next ## need to create a Node here
            print(l)

        return l

if __name__ == '__main__':
    # run a test case
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    s = Solution()
    l = s.addTwoNumbers(l1, l2)
    print(l.val)