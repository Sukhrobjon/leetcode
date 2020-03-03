# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        path = self.helper(root, sum)
        print(path)
        return True if path else False

    def helper(self, node, sum):
        # if path is None:
        #     path = []
        # when we find the path the node is leaf

        if node is None:
            return False
        # we get to the leaf
        if node.left is None and node.right is None:
            # check if it is right path
            if sum == node.val:
                return True

        left = self.helper(node.left, sum-node.val)
        right = self.helper(node.right, sum-node.val)

        return left or right


root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)


tree = Solution()
result = tree.hasPathSum(root, 18)
print(result)
