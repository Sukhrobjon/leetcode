class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            
            print(f"i: {i}, {nums1[i]}, j: {j} {nums2[j]}")
            if nums1[i] <= nums2[j]:
                # siply go to the next number in the first array
                i += 1
            else:
                nums1.insert(i, nums2[j])
                nums1.pop()
                j += 1
                i += 1
            
        while j < len(nums2):
            nums1[i] = nums2[j]
            i += 1
            j += 1


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m = 3
n = 3
obj = Solution()
result = obj.merge(nums1, m, nums2, n)
print(result)
# Output: [1, 2, 2, 3, 5, 6]
