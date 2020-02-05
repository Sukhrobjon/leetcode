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

        # add the root node into the stack
        stack.append(node)

        while stack:
            curr_node = stack[-1]  # top of the stack
            # check if node has left child
            if curr_node.left:
                # we add that node into the stack
                stack.append(curr_node.left)
            else:  # the node is the farthest left node
                # pop it
                node = stack.pop()
                # visit the node data
                visit(node.val)
                # check if we need to pop the parent of that node
                if len(stack) != 0:
                    node = stack[-1]
                    visit(node.val)
                if node.right:
                    # push it into stack
                    stack.append(node.right)


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
        stack.append(node)  # push the root node
        while stack:
            while stack[-1].left is not None:
                stack.append(stack[-1].left)
            node = stack.pop()
            visit(node.val)
            node = node.right
