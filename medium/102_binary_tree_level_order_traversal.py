# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
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
        return levels

    def level_order_traversal_v1(self, root):
        level = 0
        queue = []
        visit = []
        queue.append((root, level))
        while len(queue) != 0:
            node_level = queue.pop(0)
            # unpack the tuple value to node and level
            node, level = node_level
            # check if current node's level is added
            # if the new level has not been added
            if len(visit) < level + 1:
                visit.append([node.val])
            # if current level nodes has been added, then we need to add this node
            # at the specific location
            elif len(visit) == level + 1:
                visit[level].append(node.val)

            if node.left is not None:
                # we need to get the level of the parent node and add 1
                level_left_child = level + 1
                queue.append((node.left, level_left_child))
            if node.right is not None:
                level_right_child = level + 1
                queue.append((node.right, level_right_child))

        return visit
