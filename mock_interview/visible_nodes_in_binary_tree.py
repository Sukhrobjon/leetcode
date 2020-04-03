class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def number_visible_nodes(self, root):
        """
            
        """

        max_so_far = float('-inf')

        count = self.count_visible_nodes(root, max_so_far)

        return count

    def count_visible_nodes(self, root, max_so_far):
        """
            Counts the number of visible nodes in binary tree.
            Note: In a binary tree, if in the path from root to the node A,
            there is no node with greater value than A’s, this node A is
            visible. We need to count the number of visible nodes in
            a binary tree.
        """
        if root is None:
            return 0

        count = 1 if root.val >= max_so_far else 0
        max_so_far = max(max_so_far, root.val)
        left = self.count_visible_nodes(root.left, max_so_far)
        right = self.count_visible_nodes(root.right, max_so_far)
        return count + left + right


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(20)
    root.left.right = TreeNode(21)
    root.right.left = TreeNode(1)

    obj = Solution()
    nodes_count = obj.number_visible_nodes(root)
    print(nodes_count)

