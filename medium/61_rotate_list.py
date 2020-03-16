"""
Given a linked list, rotate the list to the right by k places,
where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head

        length = self.length(head)
        # print(length)

        if k > length:
            k = k % length

        if k == length or k == 0:
            return head
        # slow pointer
        p1 = head
        # fast pointer
        p2 = head
        # iterate the list k times to get k
        for _ in range(k):
            p2 = p2.next

        while p2.next is not None:
            p1 = p1.next
            p2 = p2.next
        # print(p1.val, p2.val)
        # unlink the list at the kth point from back
        new_head = p1.next
        p1.next = None
        # relink them
        p2.next = head
        return new_head

    def length(self, head):
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        return count



