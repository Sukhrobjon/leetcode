class Solution(object):
    def max_sub_array(self, nums):
        """
        Given an integer array nums, find the contiguous subarray (containing
        at least one number) which has the largest sum and return its sum.

        :type nums: List[int]
        :rtype: int
        """
        # NOTE: we are going to use Kadane's Algorithm
        # it is used to store the subarray indexes
        start = end = 0
        # take the first element as max subarray
        curr_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            # compare the current element to previous subarray sum
            # print(nums[i] + curr_sum, nums[i])
            curr_sum = max(nums[i], nums[i] + curr_sum)
            # print(curr_sum)
            # check if current sum less or greater than max_sum
            if max_sum < curr_sum:
                max_sum = curr_sum

        return max_sum


obj = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# nums = [-2, -3, -5, -1]
result = obj.max_sub_array(nums)
print(f"result: {result}")
