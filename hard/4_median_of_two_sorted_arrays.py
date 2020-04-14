
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
        while (count <= middle+1):
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

            count += 1

            print(nums)
            if (i == len(nums1) or j == len(nums2)):
                break
        print(nums)
        return nums[-1]

     


if __name__ == "__main__":
    nums1 = []
    nums2 = [3]

    obj = Solution()
    merged = obj.merge(nums1, nums2)
    # median = obj.findMedianSortedArrays(nums1, nums2)
    # print(f'median {median}')
    print(merged)
