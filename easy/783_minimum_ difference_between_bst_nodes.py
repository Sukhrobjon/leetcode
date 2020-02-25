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
3. Do in order traversal and Compare the adjacents, keep track of min difference 
"""


class Solution(object):
    # smallest number possible
    prev = -float('inf')
    # the biggest possible difference
    difference = float('inf')

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.in_order(root)
        return self.difference

    def in_order(self, node, prev=None, difference=None):
        if node is None:
            return

        # if prev is None and difference is None:
        #     prev = -float('inf')
        #     difference = float('inf')

        self.in_order(node.left)

        self.difference = min(node.val-self.prev, self.difference)
        # update the prev value to current node's val
        self.prev = node.val
        # move to the right side of node
        self.in_order(node.right)
