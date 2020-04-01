"""
Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        dp = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]

        for row in range(len(dp)):
            for col in range(len(dp[0])):
                print(dp[row][col])
                if row == 0 and col > 0:
                    dp[row][col] += grid[row][col-1]
                    up = dp[row-1][col]
                    left = dp[row][col-1]
                    dp[row][col] = min(up, left)
                # if we are on the edge of the grid from the top row
                elif row > 0:
                    dp[row][col] += dp[row-1][col]
                elif col > 0:
                    
                    pass
        return dp[-1][-1]
        
    def min_path_v1(self, grid):
        """
            Build the dp array as you
        """
        pass

    def min_path_v3(self, grid):
        """
            Changing the original grid, uses no extra space
            but cant find the path itself
        """
        pass

    def min_path_v2(self, grid):
        """
            fills the first row and column and fills rest
        """
        dp = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]

        dp[0][0] = grid[0][0]
        # fill the first row
        for i in range(1, len(grid[0])):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        
        # fill the first col
        for i in range(1, len(grid)):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        # fill the rest of the dp grid
        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                up = dp[row-1][col]
                left = dp[row][col-1]
        
                dp[row][col] = min(up, left) + grid[row][col]
        
        return dp[-1][-1]


matrix = [[1, 2, 5]]
# ans = 7
# path = 1->3->1->1->1
obj = Solution()
result = obj.min_path_v2(matrix)
print(result)

