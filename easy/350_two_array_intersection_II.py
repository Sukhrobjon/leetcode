"""
Given two arrays, write a function to compute their intersection.
Note:
    - Each element in the result should appear as many times as it shows
        in both arrays.
    - The result can be in any order.
link: https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""
from collections import Counter


class Solution(object):
    def intersect_v1(self, nums1, nums2):
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
        counter_1 = Counter(nums1)
        counter_2 = Counter(nums2)
        smaller = counter_1 if len(counter_1) <= len(counter_2) else counter_2
        bigger = counter_1 if len(counter_1) > len(counter_2) else counter_2
        print(smaller, bigger)
        print(f"counter 1: {counter_1}, size: {len(counter_1)}")
        print(f"counter 2: {counter_2}, size: {len(counter_2)}")
        result = []
        for key, _ in smaller.items():
            print("before if: ", key)
            if key in bigger.keys():
                print("key", key)
                occur_key = min(smaller[key], bigger[key])
                if occur_key != 0:
                    curr_num_keys = [key] * occur_key
                    # print(curr_num_keys)
                    result.extend(curr_num_keys)

        return result

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
        return list((c1 & c2).elements())


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
obj = Solution()
result = obj.intersect_v2(nums1, nums2)
print(result)
