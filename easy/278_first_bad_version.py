# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):
    def firstBadVersion(self, last_version):
        """
        :type n: int
        :rtype: int
        """
        """
        Finds the first bad version. (replication of finding the min number in
        rotated array, that was my first thought)
        Runtime: O(logn) as binary search was used
        """
        left = 1
        right = last_version
        while left < right:
            mid = left + ((right - left) // 2)
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
