class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
        
# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


# I have a bug! 
def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 
		
	# Start from the head and find the second-to-last node
    current = head
    while current.next.next: #should stop at second-to-last
        current = current.next

    current.next = None # Remove the last node by setting second-to-last node to None
    return head



head = Node(3, Node(1, Node(2, Node(4))))

current_node =remove_tail(head)
while current_node:
    print(current_node.value)
    current_node = current_node.next
