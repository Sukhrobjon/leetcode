class Solution(object):
    def duplicate_zeros(self, arr):
        """
        Given a fixed length array arr of integers, duplicate each occurrence
        of zero, shifting the remaining elements to the right.

        NOTE: The elements beyond the length of the original array are not
        written.
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr) - 1:
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 2
            else:
                i += 1

        return arr


arr = [1, 0, 2, 3, 0, 4, 5, 0]
obj = Solution()
result = obj.duplicate_zeros(arr)
print(result)
