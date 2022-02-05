class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = [[1]]

        for row in range(1, numRows):
            arr = [1]*(row+1)
            pascal.append(arr)
            for i in range(1, row):
                pascal[row][i] = pascal[row-1][i-1] + pascal[row-1][i]
            
        return pascal


row = 5
obj = Solution()
pascal = obj.generate(row)

print(pascal)

# rows = [[1]]
# for r in range(1, numRows):
#     rows.append([1] * (r+1))
#     for c in range(1, r):
#         rows[r][c] = rows[r-1][c] + rows[r-1][c-1]
# return rows
