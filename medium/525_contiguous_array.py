"""
Given a binary array, find the maximum length of a contiguous subarray with
equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0
and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
number of 0 and 1.
"""


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # this is for initial values to compare
        count_index = {0: -1}
        count = 0
        global_len = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            # if the count already in the dict then we have seen
            # same number of 0s and 1s so far
            if count in count_index:
                # update the global max
                prev_index = count_index[count]
                curr_len = i-prev_index
                global_len = max(global_len, curr_len)
            else:
                count_index[count] = i

        return global_len


nums = [1, 0, 1, 1, 0, 0]
obj = Solution()
result = obj.findMaxLength(nums)

print(result)

