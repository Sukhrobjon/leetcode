# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        return self.build_from_preorder(preorder)

    def build_from_preorder(self, preorder, left=None, right=None):

        if left is None and right is None:
            left = 0
            right = len(preorder)-1
        # base case
        if left > right:
            return None

        root = TreeNode(preorder[left])

        if left == right:
            return root
        # first we need to find the 1st bigger element than the root
        # on the right side of the all elements of that bigger element is
        # going to be the right subtree of tree
        index = left + 1
        while index <= right and preorder[index] < root.val:
            index += 1

        # left subtree
        root.left = self.build_from_preorder(preorder, left+1, index-1)
        # right subtree
        root.right = self.build_from_preorder(preorder, index, right)

        return root
