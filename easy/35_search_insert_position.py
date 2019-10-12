class Solution(object):
    def search_insert(self, nums, target):
        """
        Naive solution 40 ms
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, num in enumerate(nums):
            if num == target:
                return i
            # if target not in array
            if num > target:
                return i
            else:
                continue
        return len(nums)

    def search_insertion_v2(self, nums, target):
        """
        my solution 36ms:
        """
        if not nums or nums[0] == target:
            return 0

        left = 0
        right = len(nums)-1

        # at the beginning
        if target < nums[left]:
            return left
        # or at the end of the list
        if target > nums[right]:
            return right + 1

        # then we know the target should be inserted somewhere in the middle
        while left < right:
            middle = (left + right) // 2

            if target == nums[middle]:

                return middle

            if target > nums[middle]:
                left = middle + 1
                if target <= nums[left]:
                    return left

            # elif target < nums[middle]:
            else:
                right = middle - 1

                if target == nums[right]:
                    return right
                elif target > nums[right]:
                    return right + 1

    def search_insertion_v3(self, nums, target):
        """
        Binary search: 24ms solution from leetcode
        NOTE:You can assume there is no duplicates
        """
        if not nums:
            return 0
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        print(f"mid: {mid}, left: {left}, right: {right}")
        return left


nums = [1, 3, 5, 7]
target = 8
obj = Solution()
result = obj.search_insertion_v3(nums, target)
print(f"result: {result}, target: {target}")
