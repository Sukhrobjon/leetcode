class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        sum_dict = {0: 1}
        cumulative_sum = 0
        count = 0

        for num in nums:
            cumulative_sum += num
            diff = cumulative_sum - k
            if diff in sum_dict:
                count += sum_dict[diff]

            if cumulative_sum not in sum_dict:
                sum_dict[cumulative_sum] = 1
            else:
                sum_dict[cumulative_sum] = 1

        return count
        