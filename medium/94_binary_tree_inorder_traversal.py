# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        items = []
        if root is not None:
            self._iterative_inorder(root, items.append)

        return items

    def _iterative_inorder(self, node, visit):
        """
        Helper funtion to traverse the tree inorder
        """
        stack = []
        while stack or node:
            if node is not None:
                # push it to stack
                stack.append(node)
                node = node.left
            else:
                # pop top of the stack
                node = stack.pop()
                visit(node.val)
                # move node to the right
                node = node.right
