"""
Given a set of distinct integers, nums, return all possible subsets
AKA: (the power set).

Note: The solution set must not contain duplicate subsets.
complexity analysis O(n2^n) for oth space and runtime
Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        all_subsets = []
        current = []
        self.generate_subsets(nums, 0, all_subsets, current)

        return all_subsets

    def generate_subsets(self, nums, index, all_subsets, current):
        """
            Forms the all possible subsets of the given set of numbers
        """ 
        # base case
        print(current)
        # if index == len(nums):
        # if current not in all_subsets:
        all_subsets.append(current[:])
        # return
        for i in range(index, len(nums)):
            current.append(nums[i])
            self.generate_subsets(nums, i+1, all_subsets, current)
            current.pop()



nums = [1, 2, 2]
obj = Solution()
result = obj.subsets(nums)
print(result)