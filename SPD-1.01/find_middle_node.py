"""
    Question: Find the middle item in a singly linked list, 
    or two middle items if it contains an even number of nodes.
"""
from linkedlist import LinkedList


# refactored
def get_middle_node(ll):
    """
        It is assumed the linked list class is implemented as in class
    """
    curr_node = ll.head
    middle = ll.size // 2
    if ll.size % 2 == 0:
        for _ in range(middle - 1):  # loop through the linkedlist until we get the index
            curr_node = curr_node.next
        return (curr_node.data, curr_node.next.data)
    
    else:
        for _ in range(middle):
            curr_node = curr_node.next
        return (curr_node.data)


# original version
def find_middle_node(ll):    
    """
        It is assumed the linked list class is implemented as in class
    """

    if ll.size % 2 == 0:
        curr = head
        i = 0
        while curr:
            curr = curr.next
            i += 1
            if i == (ll.size // 2) + 1:
                return (curr.data, curr.next.data)
    else:
        curr = head
        i = 0
        while curr:
            curr = curr.next
            i += 1
            if i == (ll.size // 2) + 1:
                return curr.data

# test the function

ll = LinkedList()

print(ll)

print('Appending items:')
ll.append('A')
print(ll)
ll.append('B')
print(ll)
ll.append('C')
print(ll)
print("Find the middle with odd nodes!")
print(get_middle_node(ll))
ll.append('D')
print(ll)
print("Find the middle with even nodes!")
print(get_middle_node(ll))


