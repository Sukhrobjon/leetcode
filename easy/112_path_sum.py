# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        

    def helper(self, node, sum):
        # if path is None:
        #     path = []
        # when we find the path the node is leaf

        if node is None:
            return False
        # we get to the leaf
        if node.left is None and node.right is None and sum == node.val:
            # check if it is right path
            return True

        return self.helper(node.left, sum-node.val) or \
            self.helper(node.right, sum-node.val)
