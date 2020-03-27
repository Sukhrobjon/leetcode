class Solution(object):
    def max_product(self, nums):
        """
        Given an integer array nums, find the contiguous subarray (containing
        at least one number) which has the largest sum and return its sum.

        :type nums: List[int]
        :rtype: int
        """
        # take the first element as max subarray
        curr_prod = nums[0]
        max_prod = nums[0]

        for i in range(1, len(nums)):
            # compare the current element to previous subarray sum
            print(f"current elem: {nums[i]}")
            print(f"current product before: {curr_prod}")
            curr_prod = max(nums[i], nums[i] * curr_prod)
            print(f"current product: {curr_prod}")
            # check if current sum less or greater than max_sum
            if max_prod < curr_prod:
                max_prod = curr_prod

        return max_prod

    def max_product_v2(self, numbers):
        """
            uses curr_max, curr_min and global_max
        """
        curr_min = numbers[0]
        curr_max = numbers[0]
        global_max = numbers[0]

        for i in range(1, len(numbers)):
            temp = curr_max
            print(f"curr_max: {curr_max}, curr_min: {curr_min}")
            print(f"cur_max * num[i] -> {curr_max*numbers[i]}")
            print(f"curr_min({curr_min}) * numbers[i] -> {curr_min*numbers[i]}")
            curr_max = max(max(curr_max*numbers[i], curr_min*numbers[i]), numbers[i])
            curr_min = min(min(temp*numbers[i], curr_min*numbers[i]), numbers[i])
            print(f"curr_max: {curr_max}, curr_min: {curr_min}")
            global_max = max(curr_max, global_max)

        return global_max

obj = Solution()
# nums = [2, 3, -2, 4]
nums = [-2, 3, -4]
result = obj.max_product_v2(nums)
print(f"result: {result}")
