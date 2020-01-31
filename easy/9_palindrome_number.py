class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if number
        if x < 0 or (x % 10 == 0 and x != 0):
            print("here")
            return False

        reverse_num = 0
        while reverse_num < x:
            reverse_num = (reverse_num * 10) + (x % 10)
            x /= 10

        return x == reverse_num or x == reverse_num / 10

num = 100
obj = Solution()
print(obj.isPalindrome(num))