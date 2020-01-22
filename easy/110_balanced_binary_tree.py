# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    result = True

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # call the height
        self.get_height(root)
        return self.result
        
    def get_height(self, node):
        """
        Checks ifa binary tree in which the left and right subtrees of
        every node differ in height by no more than 1.
        """
        if node is None or self.result is False:
            return 0
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        
        if abs(left_height-right_height) > 1:
            self.result = False
        return max(left_height, right_height) + 1
