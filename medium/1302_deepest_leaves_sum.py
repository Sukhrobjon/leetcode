"""
Given a binary tree, return the sum of values of its deepest leaves.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:

        height = self.get_height(root)

        return height

    def get_height(self, root):

        if root is None:
            return 0

        left = self.get_height(root.left)
        right = self.get_height(root.right)

        height = max(left, right) + 1

        return height
