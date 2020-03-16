"""
A linked list is given such that each node contains an additional random
pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each
node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer
points to, or null if it does not point to any node.

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
"""


class Node:
    """
    # Definition for a Node.
    """
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        # store the head of cloned linked list
        cloned_head = Node(head.val)
        clone_iterator = new_head
        original_iterator = head

        # first clone the linked list ignoring the random pointers
        while original_iterator.next:
            # assign the newly created clone node 
            clone_iterator.next = Node(original_iterator.next.val)

            # move forward in both lists
            clone_iterator = clone_iterator.next
            original_iterator = original_iterator.next

        # now we copy the random pointers
        new_head = cloned_head
        old_head = head
        

        while(new_head is not None and old_head is not None):
            
            # get a reference 
            temp = old_head.next
            # point the old node to its clone
            old_head.next = new_head
            new_head.random = old_head.random
            # move the new head by one forward
            new_head = new_head.next
            # move the old head by one forward
            old_head = temp
        # get a reference to the head of clone linked list head
        c_head = cloned_head
        # now we manipulate the random pointers
        while c_head.next is not None:
            # if random points to a another node we assign it, else it stays as null
            if c_head.random.random:
                # clone head random points to its original nodes random
                # original node's random.next points to it clone node
                c_head.random = c_head.random.random.next
            
        return cloned_head
        
    def copy_random_list(self, head):
        """
        Deep copies the linked list
        """

        if head is None:
            return head
        curr = head
        while curr is not None:
            # create a new node
            new_node = Node(curr.val)
            # point the new node to the curr.next
            new_node.next = curr.next
            # link the current node to the new node
            curr.next = new_node
            # move forward
            curr = curr.next.next

        curr = head
        # now we can manimulate the random pointers
        while curr is not None:
            # check if curr random points to node or none
            if curr.random is not None:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # now we restore the original list
        curr = head
        copy = head.next
        while curr.next is not None:
            # store the reference to curr.next node
            temp = curr.next
            # skip one node
            curr.next = curr.next.next
            # move the current node iterator by one forward
            curr = temp

        return copy
