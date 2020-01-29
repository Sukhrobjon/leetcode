class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        start = 0
        end = len(matrix)-1
        while start < end:
            pos1 = [start, start]
            pos2 = [start, end]
            pos3 = [end, end]
            pos4 = [end, start]
            for i in range(start, end):
                temp1 = matrix[pos1[0]][pos1[1]]
                temp2 = matrix[pos2[0]][pos2[1]]
                temp3 = matrix[pos3[0]][pos3[1]]
                temp4 = matrix[pos4[0]][pos4[1]]

                matrix[pos1[0]][pos1[1]] = temp4
                matrix[pos2[0]][pos2[1]] = temp1
                matrix[pos3[0]][pos3[1]] = temp2
                matrix[pos4[0]][pos4[1]] = temp3

                pos1[1] += 1
                pos2[0] += 1
                pos3[1] -= 1
                pos4[0] -= 1

            start += 1
            end -= 1

        # return matrix
