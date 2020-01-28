class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # compare the first element of all string in the list
        # until find the mismatch
        # first letter of first word in the list
        # initial prefix is whole word of the 0th element of the list
        prefix = strs[0]


        for i in range(1, len(strs)):
            word = strs[i]
            bound = min(len(prefix), len(word))
            for j in range(0, bound):
                print(word)
                # print(f"prefix[j]: {prefix[j]}, word[j]: {word[j]}")
                if prefix[j] != word[j] and j == 0:
                    # print(f"prefix[j]: {prefix[j]}, word[j]: {word[j]}")
                    return ""
                elif prefix[j] != word[j]:
                    break
                
            prefix = prefix if len(prefix) <= len(word[0:j]) else word[0:j]
            print(f"pre: {prefix}")
        return prefix


strs = ["flower", "flow", "flight", 'f']
obj = Solution()
print("prefix: ", obj.longestCommonPrefix(strs))
