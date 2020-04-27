class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == n:
            return m
            
        result = m
        for num in range(m+1, n+1):
            result &= num

        return result


obj = Solution()
m, n = 5, 7
result = obj.rangeBitwiseAnd(0, 1)
print(result)