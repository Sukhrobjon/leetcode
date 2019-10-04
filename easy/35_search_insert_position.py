class Solution(object):
    def search_insert(self, nums, target):
        """
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
        Binary search
        """
        if not nums:
            return 0
        left = 0
        right = len(nums)-1
        count = 0

        # at the beginning
        if target < nums[left]:
            return left
        # or at the end of the list
        if target > nums[right]:
            return right + 1

        # then we know the target should be inserted somewhere in the middle
        while left < right:
            middle = (left + right) // 2
            count += 1
            print(f"middle: {nums[middle]}, i: {middle}")
            if target == nums[middle]:
                print("count: ", count)
                return middle

            if target > nums[middle]:
                left = middle + 1
                if target <= nums[left]:
                    print("found left")
                    return left
                print("left: ", left)
            elif target < nums[middle]:
            # elif:
                right = middle - 1
                print("right: ", right)
                if target >= nums[right]:
                    print("found right")
                    return right
        # print(f"middle: {middle}")
        return "Not found"
nums = [1, 3, 5, 6]
target = 2
obj = Solution()
result = obj.search_insertion_v2(nums, target)
print(f"result: {result}, target: {target}")
