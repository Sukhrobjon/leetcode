class Solution(object):
    def search(self, nums, target):
        """
        Suppose an array sorted in ascending order is rotated at some pivot
        unknown to you beforehand.
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        pivot = self.find_pivot_index(nums)
        # check if target is possibly in the range
        if target < nums[pivot] or target > nums[pivot-1]:
            print("not found")
            return -1
        if target >= nums[pivot] and target <= nums[-1]:
            left = pivot
            right = len(nums) - 1
        elif target <= nums[pivot-1] and target >= nums[0]:
            left = 0
            right = pivot-1
        else:
            return -1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid, nums[mid]
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def find_pivot_index(self, nums):
        """
        Suppose a sorted array A is rotated at some pivot unknown to you
        beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
        Find the minimum element. NOTE: The array will not contain duplicates.
        """
        min_num = nums[0]
        pivot_index = 0
        left = 0
        right = len(nums) - 1
        if left == right:
            return pivot_index

        while left <= right:
            mid = (left + right) // 2
            # print(nums[mid])

            if min_num > nums[mid]:
                min_num = nums[mid]
                pivot_index = mid
                right = mid - 1
            else:
                left = mid + 1

        return pivot_index

    def search_v1(self, nums, target):
        """
            Solution based on the leetcode solution
        """
        pass



nums_r = [4, 5, 6, 7, 0, 1, 2]
nums = [0, 1, 2, 4, 5, 6, 7]
single = [5]
t = 3
obj = Solution()
result = obj.search(nums_r, t)
print(result)
