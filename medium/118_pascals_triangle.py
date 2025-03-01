# class Solution(object):
#     def generate(self, numRows):
#         """
#         :type numRows: int
#         :rtype: List[List[int]]
#         """
#         pascal = [[1]]

#         for row in range(1, numRows):
#             arr = [1]*(row+1)
#             pascal.append(arr)
#             for i in range(1, row):
#                 pascal[row][i] = pascal[row-1][i-1] + pascal[row-1][i]
            
#         return pascal


# row = 5
# obj = Solution()
# pascal = obj.generate(row)

# print(pascal)

arr = [2, 4, 1, 0, 7, 3, 10, 6] # => 10, 7

max1 = max2 = float('-inf')

for num in arr:
    if num > max1:
        max2 = max1
        max1 = num
        
    elif num > max2:
        max2 = num

print(max1, max2)
