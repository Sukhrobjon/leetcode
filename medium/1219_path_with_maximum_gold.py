class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # early check
        if not grid or len(grid) == 0:
            return 0
            
        global_max = 0
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] > 0:
                    curr_max = self.find_max_gold(grid, row, col, visited)
                    if curr_max > global_max:
                        global_max = curr_max
        
        return global_max

    def find_max_gold(self, grid, row, col, visited):
        """
            Helper function to perform dfs starting given location in the grid
        """
        # bound check
        if (row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])):
            return 0
        if grid[row][col] == 0 or visited[row][col]:
            return 0
        # set is as visited
        visited[row][col] = True

        # go ahead and do dfs
        up = self.find_max_gold(grid, row - 1, col, visited)
        down = self.find_max_gold(grid, row + 1, col, visited)
        left = self.find_max_gold(grid, row, col-1, visited)
        right = self.find_max_gold(grid, row, col+1, visited)

        # set the visited back to False
        visited[row][col] = False
        # take the max of all and add the current cell value
        true_max = max(up, down, left, right) + grid[row][col]

        return true_max


matrix = [[1, 0, 7],
          [2, 0, 6],
          [3, 4, 5],
          [0, 3, 0],
          [9, 0, 20]]

obj = Solution()
result = obj.getMaximumGold(matrix)
print("Result {}".format(result))
