"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

NOTE:
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_len = 0
        for digit in nums:
            print(count, digit)
            if digit == 1:
                count += 1
            else:
                count = 0
            max_len = max(max_len, count)
        return max_len


nums = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
obj = Solution()
result = obj.findMaxConsecutiveOnes(nums)
print(result)

