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
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """

        if head is None:
            return True
        
        if root is None:
            return False

        # i wrote them more readable lines but if we dont use return values and
        # instead call them directly runs much faster, calling them directly
        # runs 112-116ms, and calling with return values runs 228ms
        # NOTE: next 4 lines are more readbable version of the return statement
        # start_from_root = self.find_path(head, root)
        # start_from_left = self.isSubPath(head, root.left)
        # start_from_right = self.isSubPath(head, root.right)
        # return start_from_root or start_from_left or start_from_right
        return self.find_path(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def find_path(self, head, root):
        """
            find a path from given root and head of the linked list
        """

        if head is None:
            return True
        if root is None:
            return False
        
        if head.val == root.val:
            return self.find_path(head.next, root.left) or self.find_path(head.next, root.right)
