# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        curr = root
        while curr:
            # check if node has children
            if curr.left is not None or curr.right is not None:
                if curr.val < curr.left.val or curr.val > curr.right.val:
                    return False
                # otherwise we call it recursively
                self.isValidBST(curr.left)
                self.isValidBST(curr.right)

        return True
