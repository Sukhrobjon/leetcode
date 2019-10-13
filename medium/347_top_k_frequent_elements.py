from collections import Counter


class Solution(object):
    def top_k_frequent(self, nums, k):
        """
        Given a non-empty array of integers, return the k most frequent
        elements.
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        NOTE: You may assume k is always valid, 1 ≤ k ≤ number of unique
        elements.
        Your algorithm's time complexity must be better than O(n log n),
        where n is the array's size.[Current solution is O(nlogn)]
        """
        # create counter dict for frequency of each number
        nums_counter = Counter(nums)
        freq = lambda x: x[1]
        sort_nums = sorted(nums_counter.items(), key=freq, reverse=True)

        result = []
        # first k most frequent integers
        for i in range(k):
            result.append(sort_nums[i][0])
        return result


nums = [1, 1, 1, 2, 2, 3]
k = 2
obj = Solution()
result = obj.top_k_frequent(nums, k)
print(result)
