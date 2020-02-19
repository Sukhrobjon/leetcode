'''
Description:
Given a singly linked list, group all odd nodes together followed by the even
nodes. Please note here we are talking about the node number and not the value
in the nodes.

You should try to do it in place. The program should run in O(1) space
complexity and O(nodes) time complexity.

Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

NOTE:
The relative order inside both the even and odd groups should remain as
it was in the input.
The first node is considered odd, the second node even and so on ...
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # store a reference
        odd_list = head
        even_list = head.next
        # we also need head of even nodes later to connect it back to odd list
        even_head = head.next
        
        # traverse it until either, odd or even list.next is none
        while odd_list.next and even_list.next:
            # store the new next nodes
            # from this 1->2->3->4->5->null
            # odd list  1->3->4->5->null
            # even list 2->3->4->5->null
            odd_list.next = odd_list.next.next
            even_list.next = even_list.next.next
            # skip to the next odd node and even nodes
            odd_list = odd_list.next
            even_list = even_list.next

        # connect the end of odd list to the head of even list
        odd_list.next = even_head

        return head
