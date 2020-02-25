# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Given a Binary Search Tree (BST) with the root node root, return the minimum
difference between the values of any two different nodes in the tree.
1. Naive solution: traverse the tree, get in order traversal. Then find all possible
difference between pairs, which takes O(n^2)
2. For each node find the closest number to it, which takes O(nlogn), because we search
for closer number in logn time for each n nodes.
3. 
"""
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
