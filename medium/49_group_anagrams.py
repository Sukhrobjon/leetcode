class Solution(object):
    def group_anagrams(self, strs):
        """
        Given an array of strings, group anagrams together. All inputs will
        be in lowercase. The order of your output does not matter.
        Args: 
            strs(list[str]): list of strings
        Returns:
            anagrams(list(list[str])): list of lists, grouped anagrams
        """
        
        offset = 97
        # uniq_key = [0] * 26
        grouped_anagrams = {}
        for word in strs:
            # we need a key for each unique anagrams in the list
            uniq_key = [0] * 26
            for char in word:
                value = ord(char) - offset
                # increment the occurance of the char in the list
                uniq_key[value] += 1
            # we need to hash the list of occurance, because list cant be hashed
            uniq_key = "".join(str(digit) for digit in uniq_key)
            # we are seeing this kinda anagram first time
            if uniq_key not in grouped_anagrams:
                grouped_anagrams[uniq_key] = [word]
            else:
                grouped_anagrams[uniq_key].append(word)

        return list(grouped_anagrams.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
obj = Solution()
result = obj.group_anagrams(strs)
print(result)