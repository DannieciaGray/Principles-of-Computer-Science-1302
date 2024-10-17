#Represents individual nodes of a Linked list 
class ListNode:
    def __init__(self,d,n = None):
        self.data = d
        self.next = n 

#1 --> 2 --> 3
node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

#takes head of linked list as param and prints all the values 
def print_linked_list(head):
    print(head.value)
    if head.next != None: #base case
        return 
    print(head.value)
    print_linked_list(head.next)

def insert_in_between(node1,node2, new_node):
    node1.next = new_node
    new_node.next = node2

def insert_in_between(node1,new_node):
    new_node.next = node1.next
    node1.next = new_node

def insert_after_at_kth_position(k,new_node):
    #insert after kth postion 

   

def insert_at_kth_position(head,k,new_node):
    #Walk to the (k-1)th node

    #insert_after_at_kth_position 


    
