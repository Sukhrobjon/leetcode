# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.height(root)[0]

    def height(self, root):
        """Finds the height of the given tree"""
        if root is None:
            # diam, height
            return 0, 0

        left_d, left_h = self.height(root.left)
        right_d, right_h = self.height(root.right)

        curr_height = max(left_h, right_h) + 1
        # diameter could pass through root, which is left_height + right
        # height, or max of left diagram and right diagram
        ans = max(left_h + right_h, left_d, right_d)
        return ans, curr_height

    def diameter_v2(self, root):
        """
            Returns the diameter of tree
        """
        diameter = [0]
        self.find_height_with_diameter_v2(root, diameter)
        return diameter[0]

    def find_height_with_diameter_v2(self, root, diameter):
        """
            finding diamter without using global variable
        """
        if root is None:
            return 0
        
        left_height = self.find_height_with_diameter_v2(root.left, diameter)
        right_height = self.find_height_with_diameter_v2(root.right, diameter)

        diameter[0] = max(diameter[0], left_height + right_height)

        return max(left_height, right_height) + 1
