# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        power = 0
        result_1 = 0
        curr = l1
        while curr.next is not None:
            result_1 += curr.val * (10 ** power)
            power += 1
            curr = curr.next
        result_1 += curr.val * (10 ** power)

        power = 0
        result_2 = 0
        curr = l2
        while curr.next is not None:
            result_2 += curr.val * (10 ** power)
            power += 1
            curr = curr.next
        result_2 += curr.val * (10 ** power)
        # print(result_1, result_2)
        result = str(result_1 + result_2)

        # build linked list

        # tail node
        head = ListNode(result[0])

        for digit in result[1:]:
            node = ListNode(digit)
            node.next = head
            head = node
        # print(head)
        return head
