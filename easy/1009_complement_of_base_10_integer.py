class Solution(object):
    def bitwiseComplement(self, num):
        """
        :type N: int
        :rtype: int
        """
        return (1 << len(bin(num)) >> 2) - num - 1
