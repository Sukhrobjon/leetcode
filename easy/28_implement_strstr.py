class Solution(object):
    def strStr(self, text, pattern):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if pattern == "":
            return 0

        starter = 0  # the starting index of the patterin in the text
        index = 0  # index for text
        subindex = 0  # index for pattern

        while index <= len(text) - 1:

            if text[index] == pattern[subindex]:
                index += 1
                subindex += 1

                if subindex == len(pattern):  # check for if we checked all index of patter
                    # starter index of the text where pattern occured 1st time
                    return starter

            else:  # mismatch found
                starter += 1  # shift the starter to next index
                index = starter
                subindex = 0  # reset the subindex

        return -1


haystack = "mississippi"
needle = "issip"
obj = Solution()
result = obj.strStr(haystack, needle)
print(result)
