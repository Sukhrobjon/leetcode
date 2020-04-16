class Solution(object):
    def sortedSquares(self, nums):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        squares = [0 for i in range(len(nums))]
        # index iterator for squares array 
        i = len(squares) - 1
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            # if calculate the absolute values of 
            if abs(nums[left]) < abs(nums[right]):
                squares[i] = (nums[right])**2
                right -= 1
            else:
                squares[i] = (nums[left])**2
                left += 1
            i -= 1
        
        return squares

    
numbers = [-7, -3, 2, 3, 11]
obj = Solution()
result = obj.sortedSquares(numbers)
print(result)
