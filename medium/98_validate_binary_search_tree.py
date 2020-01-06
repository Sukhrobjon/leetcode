# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # helper function
        return self.is_valid_bst(root)

    def is_valid_bst(self, node, lower=float('-inf'), upper=float('inf')):
        """
        Validates if tree is binary search tree using upper and lower boundry for each
        node and check against them. each node should be its upper and lower bound
        """

        if node is None:
            return True
        # if duplicate are allowed we would not check if it is equal or not.
        # it could have been (node.val <= lower or node.val > upper) if there is duplicates it goes to the left side
        if (node.val <= lower or node.val >= upper):
            return False
        return self.is_valid_bst(node.left, lower, node.val) and self.is_valid_bst(node.right, node.val, upper)


"""
SOLUTION:
1. Traverse the tree:(Either recursive or iterative)
    - Have a upper and lower bound limit for each node, and compare the node's
    value with those limits NOT with the children value.
    Time Complexity: O(n) in the worst case(When tree is actually BST) we need
    to visit all nodes and compare with upper and lower limits.
    Space Complexity: O(n) because recursion creates a stack, but languages
    take care of that.
2. In order traversal(DFS):
    - We traverse the tree in order and build a array contaning all elements of
    tree and check if it is sorted increasing order.
    Time complexity: O(n) because we need to visit all nodes
    Space complexity: O(n) we craate an array of all the nodes.
    Space can be optimized. Because we dont have to keep all the values in
    the list. We only need to check if current value is greater than
    previous one
"""

