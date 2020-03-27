class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1 for i in nums]
        right = [1 for i in nums]
        print(left)
        right[-1] = 1
        output = []
        # first we go forward and multiply everything on the right side
        for i in range(1, len(nums)):
            left[i] = nums[i-1] * left[i-1]

        for i in range(len(nums)-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]

        for i in range(len(nums)):
            output.append(right[i]*left[i])
        print(left)
        print(right)
            
        return 
        
    def product_except_self_2(self, numbers):

        output = [1 for i in numbers]

        # everything on the right side
        for i in range(1, len(numbers)):
            output[i] = output[i-1] * numbers[i-1]

        # now we go backwards and calculate the left side of number
        r_val = 1
        for i in range(len(numbers)-1, -1, -1):
            output[i] = output[i] * r_val
            r_val = r_val * numbers[i]

        return output



array = [1, 2, 3, 4, 5]
obj = Solution()
result = obj.product_except_self_2(array)
print(result)
