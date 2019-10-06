class Solution(object):
    def search(self, nums, target):
        """
        Suppose an array sorted in ascending order is rotated at some pivot
        unknown to you beforehand.
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # check if arr is empty
        result = self.find_pivot(nums, target)
        if type(result) is int:
            return result

        # otherwise set the new left and right
        left = result[0]
        right = result[1]

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1


    def find_pivot(self, nums, target):
        if not nums:
            return -1

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            print(f"mid: {mid}, num[mid]: {nums[mid]}")
            if target == nums[mid]:
                print("found")
                return mid

            elif target < nums[mid]:
                if nums[mid] > nums[mid+1]:
                    left = mid + 1
                    return [left, right]
                else:
                    right = mid - 1
            else:
                if nums[mid] < nums[mid-1]:
                    right = mid - 1
                    return [left, right]
                else:
                    left = mid + 1

        return -1

nums_r = [4, 5, 6, 7, 0, 1, 2]
# nums = [0, 1, 2, 4, 5, 6, 7]
single = [5, 1, 2]
t = 2
obj = Solution()
result = obj.search(single, t)
print(result)
