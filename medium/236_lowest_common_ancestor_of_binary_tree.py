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
        """
        # if node is none return none
        if root is None:
            return None
        # if current node is equal to p or q return that node
        if root == p or root == q:
            return root
        # left val
        left = self.lowestCommonAncestor(root.left, p, q)
        # right val
        right = self.lowestCommonAncestor(root.right, p, q)
        # if left and right is not not then we know it is the ancestor
        # if node has right and left node return a value
        # then we know that node is the lowest common ancestor
        if left and right:
            return root
        # else even if we try to return not None value, if both are none,
        # then node is none line would be triggered
        else:
            return left if left else right
