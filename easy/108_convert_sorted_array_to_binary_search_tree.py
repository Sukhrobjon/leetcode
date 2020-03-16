# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.get_middle(nums)


    def get_middle(self, nums, left=None, right=None):
        """
        Takes an array and returns the middle element
        """
        # base case
        if left is None and right is None:
            left = 0
            right = len(nums) - 1

        # check the bound
        if left > right:
            return None
        mid = (right + left) // 2
        node = TreeNode(nums[mid])
        node.left = self.get_middle(nums, left, mid-1)
        node.right = self.get_middle(nums, mid+1, right)
        return node
        

nums = [1, 2, 3, 4, 5, 6, 7]