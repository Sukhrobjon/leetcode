class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        if not grid:
            return 0
        # use stack and depth first search
        # island = 0
        max_area = 0
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 1:
                    # island += 1
                    area = self.expand_island(grid, row, column)
                    print(area, max_area)
                    max_area = max(area, max_area)
        return max_area

    def expand_island(self, grid, row, column):
        """
            Helper function to perform DFS search on the grid
        """

        # bound check
        if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[row]):
            return 0
        if grid[row][column] == 0:
            return 0

        grid[row][column] = 0

        # otherwise we will cal the function recursively
        up = self.expand_island(grid, row-1, column)  # up
        down = self.expand_island(grid, row+1, column)  # down
        right = self.expand_island(grid, row, column+1)  # right
        left = self.expand_island(grid, row, column-1)  # left

        return up + down + right + left + 1


matrix = [  
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]
        ]

obj = Solution()
result = obj.maxAreaOfIsland(matrix)
print(result)