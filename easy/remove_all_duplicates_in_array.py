class Solution(object):
    def remove_element_v1(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return nums
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == val:
                print(nums)
                # del nums[i]
                print(f"index: {i}")
                nums.pop(i)
                # nums.remove(nums[i])
        if nums[0] == val:
            nums.pop(0)
        return nums
    def remove_element_v2(self, nums, val):
        """
        """
        for num in nums:
            if num == val:
                nums.remove(num)

        return nums

nums = [3, 3]
val = 3
obj = Solution()
result = obj.remove_element_v2(nums, val)
print(f"result {result}")
