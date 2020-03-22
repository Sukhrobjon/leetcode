class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # use stack and depth first search
        island = 0
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == '1':
                    island += 1
                    self.expand_island(grid, row, column)

        return island

    def expand_island(self, grid, row, column):
        """
            Helper function to perform DFS search on the grid
        """

        # bound check
        if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[row]):
            return
        if grid[row][column] == '0':
            return
        
        grid[row][column] = '0'

        # otherwise we will cal the function recursively
        self.expand_island(grid, row-1, column) # up
        self.expand_island(grid, row+1, column)  # down
        self.expand_island(grid, row, column+1)  # right
        self.expand_island(grid, row, column-1)  # left
    
    def area_of_island(self, grid, row, column):
        """
            Find the area of an island in the matrix
        """
        if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[row]):
            return
        if grid[row][column] == '0':
            return
        
        grid[row][column] = '0'
        


obj = Solution()
grid_1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
        ]

grid_2 = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]

grid = grid_2
result = obj.numIslands(grid)
print(grid)
print(result)
