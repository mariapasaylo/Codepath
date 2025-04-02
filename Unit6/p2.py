class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next



# input head and val 
# output return frequency of the val in the linked list

#create counter variable and set it to 0
# Iterate through the linked list
## if value of current node == val
### Increment the count
# return count

def count_element(head, val): #space complexity O(1) and time complexity O(n)
    count=0 #O(1)
    pointer = head #O(1)
    
    while pointer: #O(n) where n is the number of nodes in the linked list
        if pointer.value==val: #O(1)
            count+=1 #O(1)
        pointer=pointer.next #O(1)
    
    return count

head = Node(3, Node(1, Node(2, Node(1))))
print(count_element(head,1))



# Problem 4: Find the Middle
# A variation of the two-pointer technique introduced in Unit 4 is to have a slow and a fast pointer that increment at different rates. Given the head of a linked list, use the slow-fast pointer technique to find the middle node of a linked list. If there are two middle nodes, return the second middle node.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def find_middle_element(head):
	# fast=head.next.next
    # slow=head.next

    slow,fast=head,head
    while fast is not none
    while fast.next and fast: # while fast is not none
        slow=slow.next
        fast=fast.next.next
Example Usage:

# Input List:
# 1 -> 2 -> 3
# Input: head = 1