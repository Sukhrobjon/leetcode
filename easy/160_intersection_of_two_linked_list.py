"""
Description: Write a program to find the node at which the intersection of two
singly linked lists begins.

Example: For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10,
return the node with value 8.

NOTE: In this example, assume nodes with the same value are the exact same
node objects. Do this in O(M + N) time (where M and N are the lengths of the
lists) and constant space.

Problem: https://leetcode.com/problems/intersection-of-two-linked-lists/
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_a = self.get_length(headA)
        len_b = self.get_length(headB)
        
        longer_list = len_a if len_a >= len_b else len_b
        # the difference we neet to iterate the longer list to get the same
        # length as shorter one
        k = len_a - len_b if len_a >= len_b else len_b - len_a
        if len_a >= len_b:
            for _ in range(k):
                headA = headA.next
        else:
            for _ in range(k):
                headB = headB.next

        # now we have the same length of linked lists
        while headA != headB:
            headA = headA.next
            headB = headB.next

        # return intersected node
        return headA

    def get_length(self, head):
        """
        Return the length of the linked list
        """
        count = 0

        while head is not None:
            head = head.next
            count += 1

        return count

