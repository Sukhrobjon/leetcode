class Solution(object):
    def max_product(self, nums):
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
        curr_pro = nums[0]
        max_pro = nums[0]

        for i in range(1, len(nums)):
            # compare the current element to previous subarray sum
            print(f"current elem: {nums[i]}")
            curr_pro = max(nums[i], nums[i] * curr_pro)
            print(f"current product: {curr_pro}")
            # check if current sum less or greater than max_sum
            if max_pro < curr_pro:
                max_pro = curr_pro

        return max_pro


obj = Solution()
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [-2, -1, -1]
result = obj.max_product(nums)
print(f"result: {result}")
