# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # convert the n from the end to from the beginning
        new_n = self.length(head) - k
        curr = head
        # check the target is the head
        if new_n == 0:
            head = head.next
        else:
            for _ in range(new_n - 1):
               curr = curr.next

            curr.next = curr.next.next

        return head
    
    def removeNthFromEnd_v2(self, head, k):
        """
        Use 2 pointers, since we dont know the length of the linked list
        """
        
        p1 = head
        p2 = head

        # first we need to move the p1 to k from the beginning of LL
        for _ in range(k):
            if p1 is None:
                return head
            p1 = p1.next
        
        # we want to stop the slow pointer one before the desired node
        while p1.next is not None:
            p1 = p1.next
            p2 = p2.next

        # replace the data of the node at that location with next node
        p2.val = p2.next.val
        p2.next = p2.next.next

        return head

    def length(self, head):
        curr = head
        count = 0
        while(curr):
            count += 1
            curr = curr.next
        return count
