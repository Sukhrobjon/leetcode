class Solution(object):
    def group_anagrams_main(self, strs):
        
        v1 = self.group_anagrams_v1(strs)
        v2 = self.group_anagram_v2(strs)
        
        return v2

    def group_anagram_v2(self, strs):
        """
            group anagram v2, using the helper function to encode the letters
            to its number of letters in each word.
        """
        if not strs:
            return []
        # group them
        anagrams = {}

        for word in strs:
            # decode it into letter count
            code = self.encode_to_count(word)

            if code in anagrams:
                anagrams[code].append(word)
            else:
                anagrams[code] = [word]
        # return the values only
        return list(anagrams.values())


    def encode_to_count(self, word):
        """
            Helper function for group anagrams main function to count the
            number of letters in the word.
            Takes a string and return the a string representation of each
            letter's count.
        """
        # lower case a will be the 0th index
        offset = ord('a')
        count = [0] * 26
        for letter in word:
            index = ord(letter) - offset
            count[index] += 1

        return "".join(str(digit) for digit in count)
        
    def group_anagrams_v1(self, strs):
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
result = obj.group_anagrams_main(strs)
print(result)
