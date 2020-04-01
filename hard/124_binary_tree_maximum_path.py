"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some
starting node to any node in the tree along the parent-child connections. The
path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxPathSum(self, root):
        """
            In this problem, the approach is to check 4 different
            cases
            1. node's value
            2. node's value + left child value
            3. node's value + right child value
            4. node's value + left child value + right child value
        """
    
        max_sum = float('-inf')
        self.max_path(root, max_sum)
        return max_sum

    def max_path(self, root, max_sum):

        if root is None:
            return 0

        left = max(0, self.max_path(root.left, max_sum))
        right = max(0, self.max_path(root.right, max_sum))

        max_sum = max(left+right+root.val, max_sum)

        return max(left, right, 0) + root.val
