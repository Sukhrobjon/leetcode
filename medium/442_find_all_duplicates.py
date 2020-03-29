"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements
appear `twice` and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Encoding the duplicates by making them -1 values
        """
        dups = []
        
        for i in range(len(nums)):
            
        
        


numbers = [4, 3, 2, 7, 8, 2, 3, 1]
obj = Solution()
duplicates = obj.findDuplicates(numbers)
