class Solution(object):
    def uniquePaths(self, grid):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.unique_paths_v1(grid)

    def unique_paths_v1(self, grid):
        """
            My original solution
        """
        
        # first create 2d array, 1st row and col equal to 1
        if grid[0][0] == 1:
            return 0

        dp = [[1 for j in range(len(grid[0]))] for i in range(len(grid))]

        # mark the obstacles in colums
        for j in range(len(dp[0])):
            if grid[0][j] == 1:
                while j < len(dp[0]):
                    dp[0][j] = 0
                    j += 1
                break
        # mark the obstacles in rows
        for i in range(len(dp)):
            if grid[i][0] == 1:
                while i < len(dp):
                    dp[i][0] = 0
                    i += 1
                break
        # print(dp)
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                # if there's an obstacle mark that path as 0
                if grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        print(dp)
        return dp[-1][-1]

    def unique_paths_v2(self, grid):
        # first create 2d array, 1st row and col equal to 1
        if grid[0][0] == 1:
            return 0
        
        # fill the array with zeros 
        dp = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        # mark the beginng of the path
        dp[0][0] = 1 - grid[0][0]
        
        # mark the obstacles in colums
        for i in range(1, len(dp[0])):
            # set the element at the current position
            # previous value * (1 - grid's value at the current position)
            # because once we see any obstacle on this path, there no way
            # to continue from now on so set the rest to 0
            dp[0][i] = dp[0][i-1] * (1-grid[0][i])

        # mark the obstacles in colums
        for i in range(1, len(dp)):
            dp[i][0] = dp[i-1][0] * (1-grid[i][0])
        
        print(dp)

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) * (1-grid[i][j])

        print(dp)
        return dp[-1][-1]


matrix = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
# matrix = [[1]]
obj = Solution()
result = obj.uniquePaths(matrix)
print(result)
