
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)
        # brute force solution
        middle = total // 2
        # if the new length is odd
        
        i, j = 0, 0
        nums = []
        count = 0
        while (count <= middle + 1) and (i < len(nums1) and j < len(nums2)):
            
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

            count += 1
        print(nums)
        return nums[-1]


if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]

    obj = Solution()

    median = obj.findMedianSortedArrays(nums1, nums2)
    print(f'median {median}')