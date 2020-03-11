class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return matrix
        print("Original: ")
        self.display_matrix_formatted(matrix)
        self.set_zeroes_v1(matrix)
        print("Updated: ")
        self.display_matrix_formatted(matrix)
    def set_zeroes_v1(self, matrix):
        """Zet the row and column to zero if zero is seen in that row or column"""
        # first we need to make the flag for each row and column
        row = False
        col = False
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    if i == 0:
                        row = True
                    if j == 0:
                        col = True
                    # flag that row and column to zero
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # now we need to set the column and rows to 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if (matrix[0][j] == 0 or matrix[i][0] == 0):
                    # set those row and column to 0
                    matrix[i][j] = 0
        if row:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if col:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        # self.display_matrix_formatted(matrix)
        return matrix

    def display_matrix_formatted(self, matrix):
        # print the matrix formatted
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j], end=" ")
            print()
obj = Solution()
matrix = [  
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]

m_2 = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]

m_2_expected = [
                    [0, 0, 0, 0],
                    [0, 4, 5, 0],
                    [0, 3, 1, 0]
                ]       
result = obj.setZeroes(m_2)
# print(matrix)
