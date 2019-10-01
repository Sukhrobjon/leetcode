"""
Given two arrays, write a function to compute their intersection.
Note:
    - Each element in the result must be unique.
    - The result can be in any order.
link: https://leetcode.com/problems/intersection-of-two-arrays/
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        Finds the intersection of two given array.
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(set(nums2)))


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
obj = Solution()
result = obj.intersection(nums1, nums2)
print(result)
