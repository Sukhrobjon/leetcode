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
    def deepestLeavesSum(self, root) -> int:
        if not root:
            return 0
        height = self.get_height(root)

        leaves = []
        self._get_deepest_leaves(root, 0, height, leaves)

        return sum(leaves)

    def _get_deepest_leaves(self, root, curr_level, deep_level, leaves):

        # if leaves is None:
        #     leaves = []

        if root is None:
            return None
        # print(root.val)
        self._get_deepest_leaves(root.left, curr_level+1, deep_level, leaves)
        self._get_deepest_leaves(root.right, curr_level+1, deep_level, leaves)

        if root.left is None and root.right is None:
            if curr_level + 1 == deep_level:
                # print("cur level: ",curr_level)
                # print("deep_level", deep_level)
                # print("node:", root.val)
                leaves.append(root.val)

    def get_height(self, root):

        if root is None:
            return 0

        left = self.get_height(root.left)
        right = self.get_height(root.right)

        height = max(left, right) + 1

        return height

    def _level_sum(self, root):
        """
            We perform bfs to traverse the tree, and calculate
            each levels sum
        """
        queue = [root]
        level_sum = 0
        while len(queue) != 0:
            level_sum = 0

            for i in range(len(queue)):
                # pop the value
                print("size:", len(queue))
                node = queue.pop(0)
                level_sum += node.val
                # the we add the children
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return level_sum
