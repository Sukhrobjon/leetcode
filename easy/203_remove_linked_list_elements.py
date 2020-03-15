class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        prev = None

        # check if all nodes are same values as target
        while head != None and head.val == val:
            head = head.next
        # if we removed all elements then head is None
        if head is None:
            return

        curr = head
        # count = 0
        while curr.next is not None:
            # count += 1
            if curr.next.val == val:
        
                # check if the is tail

                # prev.next = curr.next
                # curr.next = None
                curr.next = curr.next.next
                # print(f"prev: {prev.val}, curr: {curr.val}")
            else:
                # prev = curr
                curr = curr.next

        # print("count: ", count)
        return head
