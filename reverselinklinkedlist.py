# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next  # Agle node ko bacha lo
        current.next = prev       # Pointer ko ulta ghuma do
        prev = current            # Prev ko aage badhao
        current = next_node       # Current ko aage badhao
        
    return prev  # Prev ab naya head ban chuka hai