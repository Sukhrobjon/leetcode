class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        Optimized version
        """

        # first occurance of 1
        left = 0
        # last occurance of 1
        right = len(nums) - 1
        i = 0

        while i <= right:
            if nums[i] == 0:
                # swap i with left most item
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1

            elif nums[i] == 1:
                # print(i)
                # just go to the next element
                i += 1
            # if the num is 2 swap it with the right most element
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1


obj = Solution()
nums = [2, 0, 2, 1, 1, 0]
obj.sortColors(nums)
print("result: {}".format(nums))