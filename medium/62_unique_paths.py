class Solution(object):
    def uniquePaths(self, col, row):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # first create 2d array, 1st row and col equal to 1

        dp = [[1 for j in range(col)] for i in range(row)]
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        print(dp)
        return dp[-1][-1]

    
obj = Solution()
result = obj.uniquePaths(1, 1)
print(result)
