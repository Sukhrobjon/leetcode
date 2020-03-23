# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator:

    def __init__(self, root):
        
        self.stack = []
        self._inorder_traversal(root)

    def next(self):
        """
        @return the next smallest number
        """
        next_node = self.stack.pop()
        if next_node.right:
            # we need to call the in order traversal and pass the right child
            self._inorder_traversal(next_node.right)
        return next_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        # as long as stack has item
        return len(self.stack) > 0

    def _inorder_traversal(self, node):
        while node:
            self.stack.append(node)
            node = node.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
