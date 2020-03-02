"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two
given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor
is defined between two nodes p and q as the lowest node in T that has both
p and q as descendants (where we allow a node to be a descendant of itself).”

NOTE:
    All of the nodes' values will be unique.
    p and q are different and both values will exist in the BST.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        Runtime: O(h) h is the height of the tree
        """

        # if root data is greater than the max of the
        # two given node, then the nodes are exist in the left subtree
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        # if root data is less than the minimum of two nodes
        # then we know the values are in the right side of the root
        elif root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        # otherwise that current node itself is the common ancestor
        else:
            return root

