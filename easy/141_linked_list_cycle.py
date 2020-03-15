# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        p1 = head
        p2 = head

        # stops when p1 and p2 points to the same node
        while p1.next != p2.next:
            # if any pointer points to none then there is no cycle
            if p1.next is None or p2.next is None:
                return False
            p1 = p1.next
            p2 = p2.next.next

        return True
            