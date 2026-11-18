# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    values = []
    current = head
    # Linked list ki saari values ek list mein store kar lo
    while current:
        values.append(current.val)
        current = current.next
        
    # Check karo ki list aur uska reverse barabar hai ya nahi
    return values == values[::-1]