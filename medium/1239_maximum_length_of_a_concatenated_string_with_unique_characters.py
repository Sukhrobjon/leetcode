class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        if not arr:
            return 0
        if len(arr) == 1:
            return len(arr[0])
        result = [0]
        self.max_unique(arr, 0, "", result)

        return result[0]
        
    def max_unique(self, arr, index, current, result):
        """Finds the max possible length of s"""

        if index == len(arr) and (self.unique_chars(current) > result[0]):
            result[0] = self.unique_chars(current)
            return

        if index == len(arr):
            return

        self.max_unique(arr, index + 1, current, result)
        self.max_unique(arr, index + 1, current+arr[index], result)

    def unique_chars(self, word):
        """
            Returns the length of the word if all chars are unique
            else -1
        """
        count = [0] * 26
        offset = ord('a')
        for char in word:
            index = ord(char) - offset
            count[index] += 1
            if count[index] > 1:
                return -1

        return len(word)


arr = ["un", "iq", "ue"]
obj = Solution()
result = obj.maxLength(arr)
print(result)
