class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            word = strs[i]
            print("word: ", word)
            prefix = self.common_prefix(prefix, word)
            print("each word", prefix)
            # if we have empty prefix no need to compare the rest
            if prefix == "":
                return ""
        
        return prefix

    def common_prefix(self, word_1, word_2):
        """
        Returns the common prefix of two words
        """
        bound = min(len(word_1), len(word_2))
        # if one of the strings are empty string
        if bound == 0:
            return ""
        for i in range(bound):
            if word_1[i] != word_2[i] and i == 0:
                return ""
            elif word_1[i] != word_2[i]:
                return word_1[0:i]
        return word_1[0:bound]
# strs = ["flower", "flow", "flight", "d"]
strs = ["x", "x"]
# ["c","c"], ["", "b"]
obj = Solution()
print("prefix: ", obj.longestCommonPrefix([]))
print("two word: ", obj.common_prefix(strs[0], strs[1]))


