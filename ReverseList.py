class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    
    prev = None # Initialize previous node as None
    curr = head # Start with the head of the list

    while curr:
        temp_next = curr.next # Store the next node temporarily
        curr.next = prev # Reverse the pointer of the current node to point to the previous node
        prev = curr  # Move previous and current pointers one step forward
        curr = temp_next
    
    return prev # The previous node will now be the head of the reversed list