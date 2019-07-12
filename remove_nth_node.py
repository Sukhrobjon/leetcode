# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):

    def remove_nth_from_end(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # convert the n from the end to from the beginning
        new_n = self.length(head) - n
        curr = head
        # check the target is the head
        if new_n == 0:
            head = head.next
        else:
            # stop right before the target to be deleted
            for _ in range(new_n - 1):
               curr = curr.next
            
            # skip that nth node
            curr.next = curr.next.next

    
    def length(self, head):
        """Return the length of the linked list"""
        curr = head
        count = 0
        while(curr):
            count += 1
            curr = curr.next
        return count
