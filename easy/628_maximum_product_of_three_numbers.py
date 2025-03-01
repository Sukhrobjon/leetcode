class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        # possible solutions
        # 1) brute force try all three combination(O(n^3))
        # 2) Sort and take max(min1*min1*max1, max1*max2*max3)
        # 3) use one pass and keep track of min1, min2, max1, max2, max3
        # 4) extended of the problem use heap, nlargest

        nums.sort()
        # two min times the largest number or last three largest number,
        # because there might be negative number
        # at the most left side
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])
