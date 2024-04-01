 #Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
       dummy = output = ListNode() 

       while l1 and l2: #while l1 and l2 are not null
          if l1.val < l2.val: # if the value in l1 is less than l2 we add l1 value to the output
             output.next = l1
             l1 = l1.next # move the pointer to next value in l1

          else:
             output.next = l2  # if l2 less than l1 we add l2 value to the output
             l2 = l2.next
             output = output.next # move the pointer to next value in l2

          if l1: # if only l1 remains, add the rest of l1 to the output
             output.next = l1
          elif l2: # if only l2 remains , add the rest of l2 to the output
             output.next = l2
          
          return dummy.next           
       