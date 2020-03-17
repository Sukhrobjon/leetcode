# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return head
        return self.build_tree(head, tail=None)

    def find_middle(self, head, tail):
        """
            Find the middle node in the linked list given head and tail node
        """
        slow = head
        fast = head

        while fast is not tail and fast.next is not tail:
            # slow move one step ahead
            slow = slow.next
            fast = fast.next.next
        if slow:
            return slow
        else:
            return None

    def build_tree(self, head, tail=None):
        # base case
        if head == tail:
            return None

        mid = self.find_middle(head, tail)
        # create a node
        root = TreeNode(mid.val)
        # left side from the mid val
        root.left = self.build_tree(head, mid)
        # right side from the mid value
        root.right = self.build_tree(mid.next, tail)

        return root
