"""
Given a binary tree, return the bottom-up level order traversal of its nodes'
values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def levelOrderBottom(self, root):

        if root is None:
            return []

        levels = self.level_order_v2(root)

        return levels

    def level_order_v2(self, root):
        """
            We perform bfs to traverse the tree, and calculate
            each levels sum
        """
        queue = deque([root])
        levels = []
        curr_level = []
        while len(queue) != 0:
            # for each level
            curr_level = []
            for i in range(len(queue)):
                # pop the value

                node = queue.popleft()
                curr_level.append(node.val)
                # the we add the children
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            levels.append(curr_level)
        return levels[::-1]
