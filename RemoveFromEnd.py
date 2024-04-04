from typing import Optional
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head : Optional[ListNode], n: int) -> Optional[ListNode]:
         dummy = ListNode() #create a dummy node at the beginning of the list
         dummy.next = head  
         ahead = behind = dummy # set 2 pointers at the dummy node

         for _ in range(n+1): # loop runs from 0 to n, inclusive
              ahead = ahead.next # ahead is moved n+1 positions

         while ahead: # while ahead reaches the end of the list, ahead and behind are moved to the next position       
              behind = behind.next
              ahead = ahead.next   

         behind.next = behind.next.next # at the point where ahead goes out of the list, behind skips one value ahead
         return dummy.next       # returns the list excluding the skipped value 

               