class Solution(object):
    def remove_duplicates(self, nums):
        """Removes duplicate number from sorted array in place
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == nums[i-1]:
                # print(f"num[i] {nums[i]}, [i+1] {nums[i+1]}")
                del nums[i-1]

        return nums


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
empt = []
obj = Solution()
print(obj.remove_duplicates(empt))
