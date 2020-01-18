class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # naive solution
        count = 0
        com_str = []
        for i in range(len(chars)+1):
            count += 1
            if (chars[i] != chars[i+1] or (i + 1 >= len(chars))):
                com_str.append(chars[i])
                com_str.append(count)
                count = 0

        return com_str

obj = Solution()
chars = ["a", "a", "b", "b", "c", "c", "c"]
result = obj.compress(chars)
print(result)
