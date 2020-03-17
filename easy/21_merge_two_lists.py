# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        
        # create new head as dummy pointer to store the new head
        # and curr to iterate
        new_head = curr = ListNode(0)

        while l1 is not None and l2 is not None:
            
            if l1.val <= l2.val:
                curr.next = l1
                # move the l1 one the right
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            # move the current pointer
            curr = curr.next
        
        # assign the leftover list
        curr.next = l1 if l1 is not None else l2

        return new_head.next
        