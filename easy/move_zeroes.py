class Solution(object):
    def move_zeroes(self, nums):
        """
        Given an array nums, write a function to move all 0's to the end of it
        while maintaining the relative order of the non-zero elements.
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # counter for non zero elements
        count = 0

        # shifting non-zero elements to left
        for i, num in enumerate(nums):
            if num != 0:
                nums[count] = nums[i]
                count += 1

        # fill the rest of the array with 0
        for i in range(len(nums)-count):
            nums[count] = 0
            count += 1

        return nums


nums = [0, 0, 1]
# nums = [0, 1, 0, 3, 12]
obj = Solution()
result = obj.move_zeroes(nums)
print(result)
