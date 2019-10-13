"""
    Given an array of integers, find the two numbers such that 
    they add up to a specific target.
    You may assume that each input would have exactly one solution.
"""
class Solution(object):
    def two_sum_sorted_array(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        this solution works if the array is sorted
        """
        start = 0
        end = len(nums) - 1
        while start < end:
            print("start: {}, end: {}".format(start, end))
            sums = nums[start] + nums[end]
            print("sums: ", sums)
            if sums == target:
                
                return (start, end)
            end -= 1
        return ()
    def two_sum_with_index(self, nums, target):
        """
            Given nums = [2, 7, 11, 15], target = 9,
            Because nums[0] + nums[1] = 2 + 7 = 9,
            return [0, 1].

            Running Time: O(n) bc it runs number of items in the list
            Space Complexity: O(n) bc Dictionary is used to store the item and its index
        """
        pair_dict = {}
    
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in pair_dict:
                return [pair_dict[diff], i]
            else:
                pair_dict[nums[i]] = i

        return []

    def two_sum_with_num(self, nums, target):
        """
            Given nums = [2, 7, 11, 15], target = 9,
            2 and 7 is the answer bc 2 + 7 = 9
            return [2, 7]

            Running Time: O(n) bc it runs itertate through the list once
            Space Complexity: O(n) bc set is used to store the number
        """
        pair_set = set()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in pair_set:
                return [diff, nums[i]]
            else:
                pair_set.add(nums[i])

        return []


nums = [2, 3, 3, 15]
target = 17
obj = Solution()
print(obj.two_sum_with_num(nums, target))
