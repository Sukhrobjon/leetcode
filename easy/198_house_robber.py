class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_max = nums[0]
        if len(nums) >= 2:
            current_max = max(nums[0], nums[1])

        for i in range(len(2, nums)):

            current_house = nums[i]
            window_min = i - 2
