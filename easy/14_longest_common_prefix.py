class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # compare the first element of all string in the list
        # until find the mismatch
        # first letter of first word in the list
        prefix = strs[0]
        common_index = 0
        for i in range(1, len(strs)-1):
            

        return common_index


strs = ["flower", 'ffff', "flow", "flight"]
obj = Solution()
print("prefix: ", obj.longestCommonPrefix(strs))
