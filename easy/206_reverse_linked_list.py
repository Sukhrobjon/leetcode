# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        next_node = None

        while curr is not None:
            # store the next node
            next_node = curr.next
            # reverse the pointer(actual reversing here)
            curr.next = prev
            # now move the prev and curr one forward
            prev = curr
            curr = next_node
        # set the head to the node at the end originally
        head = prev
        return head
