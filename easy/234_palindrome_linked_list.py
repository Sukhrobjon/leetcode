# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True

        # first we need to reverse the linked list till middle of it
        # head of the reversed half of the linked list
        prev = None
        # these to pointer to keep track of getting the middle of LL
        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            # set the next node to the curr. next
            fast = fast.next.next
            # store slow node first
            temp = slow
            # move the slow pointer forward by one step(node)
            slow = slow.next
            # set the temp next to prev node
            temp.next = prev
            # update the prev node to current
            prev = temp

        # if fast is not None then linked list is odd length
        # we should ignore the middle node
        if fast:
            slow = slow.next
        # iterate the list until it reaches the end or we find unmatch
        while prev and (prev.val == slow.val):
            # move from the middle of the list toward two edges
            # rev head for from right to left and slow is for left to right
            prev = prev.next
            slow = slow.next

        return True if prev is None else False
