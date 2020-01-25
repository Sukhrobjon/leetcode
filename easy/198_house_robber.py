class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        curr_incl = nums[0]
        exc = 0

        for i in range(1, len(nums)):
            temp = curr_incl
            curr_incl = max(curr_incl, nums[i] + exc)
            exc = temp

        return curr_incl


nums = [2, 7, 9, 3, 1]
obj = Solution()
result = obj.rob(nums)
print("Result:", result)