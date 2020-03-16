# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # dummy data at the beginning of head
        prev = ListNode(0)
        curr = head
        # store reference to new head
        new_head = next_node = head.next

        while curr.next is not None:
            # temp
            temp = next_node.next
            # swap the pointers 
            next_node.next = curr
            curr.next = temp
            # 
            prev.next = next_node
            # move all pointers for next iterations
            prev = curr
            curr = curr.next
            next_node = curr.next

        return new_head