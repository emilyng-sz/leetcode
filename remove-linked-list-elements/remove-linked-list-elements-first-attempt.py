# Not a working solution. Needs to be cleaned and annotated

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        '''
        # attempt to write using lists for learning
        lst = head # assume
        for i in range(len(lst)): # create pointer that goes through each element 
            if lst[i] == val: # if not pointer value not equal current, current skips it and waits to attach to NEXT current
                del lst[i] # OR instead, delete by dropping curr.next and setting to pointer if it is
            return lst
        '''

        '''pointer = head
        curr = dummy = ListNode()

        while pointer is not None:
            print(curr.val, pointer.val)
            if pointer.val != val:
                curr.next = pointer
                curr = curr.next
            pointer = pointer.next
            
        return dummy.next'''
        curr = dummy = ListNode()

        while head is not None:
            if head.val == val: # dont want this 
                curr.next = head.next
                curr = curr.next
            else:
                curr.next = head 
                curr = curr.next
            head = head.next

        return dummy.next

        
        '''dummy = newHead = ListNode()
        while head is not None:
            if head.val is not val:
                newHead.next = head
                newHead = newHead.next
            head = head.next

        return dummy.next'''

if __name__ == '__main__':
    # run a test case
    l1 = ListNode(1, ListNode(2, ListNode(6, ListNode(4))))
    s = Solution()
    l = s.removeElements(l1, 2)
    print(l.val)