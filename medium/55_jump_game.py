"""
Given an array of non-negative integers, you are initially positioned at the
first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: 
You will always arrive at index 3 no matter what. Its maximum
jump length is 0, which makes it impossible to reach the last index.
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # we can start from the back of the array and check
        # if it is possible to reach it from index - 1
        last_good_index = len(nums)-1

        # iterate the array backwards
        for i in range(len(nums)-1, -1, -1):
            # if we can get from the current index to last good index
            if (i + nums[i]) >= last_good_index:
                print(last_good_index)
                last_good_index = i
        print(last_good_index)
        return last_good_index == 0


numbers = [2, 3, 1, 1, 4]  # true
# numbers = [0, 3, 1, 1, 4]  # false
obj = Solution()
result = obj.canJump(numbers)
print(result)
