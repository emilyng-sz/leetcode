# This is not a working solution.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create new LinkedList as result
        new = ListNode(0)
        
        while list1 is not None and list2 is not None:
            if list1 is not None or list1.val < list2.val: # this will not work
                new.next = ListNode(list1.val)
                list1 = list1.next 
            elif list2 is not None:
                new.next = ListNode(list2.val)
                list2 = list2.next
            new = new.next
        
        return new.next

       

if __name__ == '__main__':
    # run a test case
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    s = Solution()
    l = s.mergeTwoLists(l1, l2)
    print(l.val)

        