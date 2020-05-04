from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False

        ransom = Counter(ransomNote)
        maga = Counter(magazine)

        for letter in ransom:
            if ransom[letter] > maga[letter]:
                return False

        return True
