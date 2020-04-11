class Solution(object):
    def backspaceCompare(self, str1, str2):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # first reform the word

        word1 = self.form_original_str(str1)
        word2 = self.form_original_str(str2)
        # print(word1, word2)
        if self.compare_two_strs(word1, word2):
            return True
        return False

    def form_original_str(self, word):
        """
            Form the string after backspace pressed
        """
        output = []
        for char in word:
            # print(f'output {output}')
            if char != '#':
                # we put it into final form
                output.append(char)
            else:
                if output:
                    output.pop()

        return output

    def compare_two_strs(self, word1, word2):

        if len(word1) != len(word2):
            return False

        for i in range(len(word1)):
            if word1[i] != word2[i]:
                return False
        return True


str1 = "a##c"
str2 = "#a#c"
obj = Solution()
result = obj.backspaceCompare(str1, str2)
print(result)
