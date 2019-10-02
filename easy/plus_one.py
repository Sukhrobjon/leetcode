class Solution(object):
    def plus_one(self, digits):
        """
        Given a non-empty array of digits representing a non-negative integer,
        plus one to the integer.
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ""
        for i in digits:
            num += str(i)
        plus_1 = int(num) + 1
        return list(map(int, str(plus_1)))


digits = [9,9,9]
obj = Solution()
result = obj.plus_one(digits)
print(result)