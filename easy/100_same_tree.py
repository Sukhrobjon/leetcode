# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSameTree(self, p, q) -> bool:

        return self.check(p, q)

    def check(self, p, q):
        """Check if two trees are identical"""

        if p is None and q is None:
            return True

        if p is not None and q is not None:

            data = p.val == q.val
            left = self.check(p.left, q.left)
            right = self.check(p.right, q.right)

            return data and left and right

        else:
            return False
