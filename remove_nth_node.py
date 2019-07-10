# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):

    def removeNthFromEnd(self, head, n):
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
            for _ in range(new_n - 1):
               curr = curr.next
            
            curr.next = curr.next.next

    
    def length(self, head):
        curr = head
        count = 0
        while(curr):
            count += 1
            curr = curr.next
        
