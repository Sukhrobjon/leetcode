from collections import Counter


class Solution(object):
    def intersect_v2(self, nums1, nums2):
        """
        Function to compute their intersection of given two arrays
        Note:
            - Each element in the result should appear as many times as it
            shows in both arrays.
            - The result can be in any order.
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        result = (c1 & c2)
        print(c1)
        print(c2)
        
        print(f"dict comparison: {result}")
        return list((c1 & c2).elements())


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
obj = Solution()
result = obj.intersect_v2(nums1, nums2)
print(result)
