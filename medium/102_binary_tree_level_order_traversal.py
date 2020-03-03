# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        # counter for level
        level = 0
        queue = []
        # store the all the nodes grouped by the levels
        visit = []
        # put the root of the tree into queue with its level which is 0
        queue.append((root, level))
        while len(queue) != 0:
            # pop the node with its corresponding level
            node_level = queue.pop(0)
            # unpack the tuple value to node and level
            node, level = node_level
            # check if current node's level is added
            if len(visit) < level + 1:
                # simple append this node value as a new level
                visit.append([node.val])
            # if some of the current level nodes has been added, then we need
            # to add this node at its level position
            elif len(visit) == level + 1:
                visit[level].append(node.val)
        
            if node.left is not None:
                # we need to get the level of the parent node
                # and add 1 to it left child
                level_left_child = level + 1
                queue.append((node.left, level_left_child))
            if node.right is not None:
                # we need to get the level of the parent node
                # and add 1 to it right child
                level_right_child = level + 1
                queue.append((node.right, level_right_child))

        return visit
