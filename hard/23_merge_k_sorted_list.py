# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # dummy node to store the new head
        new_head = curr = ListNode(0)
        last_head = False
        # loop through the list and convert the lists until we have one head left
        while last_head is False:
            min_index, last_head = self.get_min_index(lists)
            print(f"min_index: {min_index}, last_head: {last_head}")
            node = lists[min_index]
            print(node.val)
            curr.next = node
            print(curr.val, curr.next.val)
            node = node.next
            print(node.val)
            curr = curr.next
            print(curr.val)
            if last_head:
                head = True
        # if it there is only one linked list left in lists
        min_index, last_head = self.get_min_index(lists)
        node = lists[min_index]
        curr.next = node
        return new_head.next

    def get_min_index(self, linked_lists, curr_min=None):
        """
            Find the minimum head in the list of heads,
            it returns the index of the minimum head, also it indicates
            if there is only 1 head left, return index and True, otherwise
            it just returns the min_index and False
        """
        if curr_min is None:
            curr_min = float('inf')
        # counter if there is only one head left in the array
        last_head = 0
        # flag if there is only one head left in the array
        one_head_left = False
        min_index = 0
        for index, head in enumerate(linked_lists):
            if head and head.val < curr_min:
                curr_min = head.val
                min_index = index
            elif head is None:
                last_head += 1

            if last_head == len(linked_lists) - 1:
                one_head_left = True
                break

        # if there is only 1 head left, we can just link it to existing list
        if one_head_left:
            for index, head in enumerate(linked_lists):
                # found the only not-None head
                if head:
                    # return its index
                    return index, True
        return min_index, False

# list a
a = ListNode(1)
a.next = ListNode(4)
a.next.next = ListNode(5)
a.next.next.next = ListNode(7)

# list b
b = ListNode(2)
b.next = ListNode(3)
b.next.next = ListNode(4)

l_lists = [a, b]
print(len(l_lists))
obj = Solution()
result = obj.mergeKLists(l_lists)
# while result:
#     print(f"result node {result.val}")
#     result = result.next
    
print(f"result node {result.val}")
print(f"result node {result.next.val}")
print(f"result node {result.next.next.val}")
print(f"result node {result.next.next.next.val}")

