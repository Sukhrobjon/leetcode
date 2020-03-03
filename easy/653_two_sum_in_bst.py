# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        result = self.helper_find_target(root, k)
        print(result)
        return True if result[1] else False

    def helper_find_target(self, node, k, compliments=None, pairs=None):
        """
        Helper function to traverse the tree and find the pairs
        """
        if compliments is None and pairs is None:
            # to store the compliments
            compliments = set()
            # to store all the pairs
            pairs = []

        if node is None:
            return False, pairs

        # check if node.val is in compliments set
        if node.val in compliments:
            pairs.append((node.val, k-node.val))
            return True, pairs
        # otherwise we add the val into the compliments
        compliments.add(k-node.val)
        left = self.helper_find_target(node.left, k, compliments, pairs)
        right = self.helper_find_target(node.right, k, compliments, pairs)

        return left or right

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(18)

tree = Solution()
result = tree.findTarget(root, 19)
print(result)
