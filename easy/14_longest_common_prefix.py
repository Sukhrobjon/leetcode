class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # if not strs:
        #     return ""
        # # first letter of first word in the list
        # # initial prefix is whole word of the 0th element of the list
        # prefix = strs[0]

        # # iterate through list of words
        # for i in range(1, len(strs)):
            
        #     word = strs[i]
        #     if len(word) == 0:
        #         return ""
        #     # compare the jth element of each word against the prefix[j]
        #     for j in range(len(word)):
        #         print(word)
        #         # print(f"prefix[j]: {prefix[j]}, word[j]: {word[j]}")
        #         # no common prefix when the 0th element doesnt match
        #         if prefix[j] != word[j] and j == 0:
        #             # print(f"prefix[j]: {prefix[j]}, word[j]: {word[j]}")
        #             return ""
        #         # unmatch
        #         elif prefix[j] != word[j]:
        #             break
        #     # update the prefix, choose min of length
        #     prefix = prefix if len(prefix) < len(word[0:j]) else word[0:j]
        #     print(f"pre: {prefix}")
        # return prefix
        def longest_common_prefix(self, strs):
            """
            
            """

# strs = ["flower", "flow", "flight"]
strs = ["b", ""]
# ["c","c"], ["", "b"]
obj = Solution()
print("prefix: ", obj.longestCommonPrefix(strs))


