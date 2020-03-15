# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        # slow pointer
        p1 = head
        # fast pointer
        p2 = head
        is_cycle = False
        # if any poiter is none then there is no cycle
        while p2 is not None and p2.next is not None:
            p1 = p1.next
            p2 = p2.next.next
            # if poiters are the same then we found the cycle
            if p1 == p2:
                # print("p1: {}, p2: {}".format(p1.val, p2.val))
                is_cycle = True
                break

        # check if there is cycle
        if is_cycle:
            # reset the p1 back to head
            p1 = head
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next
                # print(p1.val)
                # print(p2.val)
            return p1
        else:  # no cycle detected
            return None
