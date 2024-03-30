#Given head, the head of a linked list, determine if the linked list has a cycle in it.
#There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
#Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
#Return true if there is a cycle in the linked list. Otherwise, return false.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head: ListNode) -> bool:
        slow,fast = head, head # starting the slow and fast pointer at the same position

        while fast and fast.next:
            slow = slow.next # shifted by 1 point
            fast = fast.next.next # shifted by 2 points
            if slow == fast: # if both the pointers meet at some point in the loop, there exist a cycle
                return True

        return False     
            
