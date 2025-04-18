# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. 
# The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.
# The most significant bit is at the head of the linked list.

# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10  2^2 2^1 2^0 = 1 + 0* + 1*1 = 5

#Input: head, node contains 1 or 0
#Output: decimal value of the number in the linked list

#What does it mean to be the most significant bit? leftmost bit then fill in the rest of the bits with 0s

# traverse the linked list
# Store each node value in a queue
# Helper funcition to convert binary to decimal

def getDecimalValue(head):
    # Initialize decimal value
    decimal_value = 0
    
    # Traverse the linked list
    while head:
        # Shift left by 1 (multiply by 2) and add the current node's value
        decimal_value = (decimal_value << 1) | head.val
        #num = num * 2 + head.val
        head = head.next
    
    return decimal_value

#create linked list node class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
ListNode1 = ListNode(1)
ListNode2 = ListNode(0) 
ListNode3 = ListNode(1)
ListNode1.next = ListNode2
ListNode2.next = ListNode3

print(getDecimalValue(ListNode1)) # Output: 5