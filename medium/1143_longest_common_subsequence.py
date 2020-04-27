class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        row, col = len(text1), len(text2)

        dp = [[0 for j in range(col+1)] for i in range(row+1)]

        for i in range(row):
            for j in range(col):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

        return dp[-1][-1]
