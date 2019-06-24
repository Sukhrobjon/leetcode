"""
    Question: Find the middle item in a singly linked list, 
    or two middle items if it contains an even number of nodes.
"""
from linkedlist import LinkedList
def find_middle_node(ll):
    """
        it is assumed the linked list class is implemented as in class
    """
    
    if ll.size % 2 == 0:
        curr = head
        i = 0
        while curr:
            curr = curr.next
            i += 1
            if i == (ll.size // 2) + 1
                return (curr.data, curr.next.data)
    else:
        curr = head
        i = 0
        while curr:
            curr = curr.next
            i += 1
            if i == (ll.size // 2) + 1
                return curr.data


