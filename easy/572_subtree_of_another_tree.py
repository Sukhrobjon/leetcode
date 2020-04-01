# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if t is None:
            return True
        if s is None:
            return False
        # it might start from the root
        if self.is_identical(s, t):
            return True
        # else we look for the starting point of the second tree in main tree
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def is_identical(self, s, t):
        """
            takes two nodes and detemines if both tree's are identical
            from that point on
        """

        if s is None and t is None:
            return True

        if s is None or t is None:
            return False

        return s.val == t.val and self.is_identical(s.left, t.left) and self.is_identical(s.right, t.right)
