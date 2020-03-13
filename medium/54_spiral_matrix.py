class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row, col = 0, len(matrix[0])-1
        right = len(matrix[0])
        left = right - 1
        # number of row
        down = len(matrix)-1
        up = down - 1
        spiral = []
        while right > 0:
            # go to the right
            for i in range(right):
                num = matrix[row][i]
                print("right: ", num)

                spiral.append(num)
            # put the row to the bottom
            print("after right:", spiral)
            # go to the down
            for i in range(1, down+1):
                num = matrix[i][col]
                print("down: ", num)
                spiral.append(num)

            print("after down:", spiral)
            print(f'before -> row: {row, }col: {col}')
            row = col - 1
            print(f'after -> row: {row, }col: {col}')
            # go left
            print(f"left: {left}")
            for i in range(left-1, -1, -1):
                num = matrix[row][i]
                print("i: {row}, j: {i}")
                print("left: ", num)
                spiral.append(num)

            print("after left:", spiral)
            print(f'before -> row: {row, }col: {col}')
            col = row
            print(f'after -> row: {row, }col: {col}')
            for i in range(up, -1, -1):
                num = matrix[i][col]
                print("up: ", num)
                spiral.append(num)
            print("after up:", spiral)
            right -= 2
            down -= 2
            left -= 2
            up -= 2
            # break

        return spiral

    def spiral_order(self, matrix):
        """
        Print matrix in a spiral order
        """
        # k for row m for column
        k, m = 0, 0
        last_row = len(matrix) - 1
        last_col = len(matrix[0]) - 1
        spiral = []
        while (k<= last_row and m <= last_col):
            # from left to right
            for i in range(m, last_col + 1):
                num = matrix[k][i]
                spiral.append(num)
            # increment the row to move one down
            k += 1

            # move from up to bottom
            for i in range(k, last_row + 1):
                num = matrix[i][last_col]
                spiral.append(num)
            last_col -= 1

            if k <= last_row:
                # move from right to left
                for i in range(last_col, m-1, -1):
                    num = matrix[last_row][i]
                    spiral.append(num)
                last_row -= 1
            
            if m <= last_col:
                for i in range(last_row, k-1, -1):
                    num = matrix[i][m]
                    spiral.append(num)

                m += 1

        return spiral

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
# print(matrix[1][2])
output = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


obj = Solution()
result = obj.spiralOrder(matrix)
print(f"output -> {result}")
