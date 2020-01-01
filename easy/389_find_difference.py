class Solution(object):
    def find_the_difference(self, s, t):
        """
        Find the difference between two strings
        :type s: str
        :type t: str
        :rtype: str
        """
        # NOTE:since the other word 't' is shuffled version of 's'
        # NOTE:we should iterate both strings, count the occurance of letters
        
        offset = 97  # ascii value of lowercase a

        # create array for each letter, we are using 26 letters because it is
        # guaranteed to be only lowercase letters
        s_count = [0] * 26
        t_count = [0] * 26

        # since the length of the strings aren't equal, use two different loop
        for char in s:
            # get the ascii value of char so we can increment the occurance
            val = ord(char) - offset
            s_count[val] += 1
        for char in t:
            # get the ascii value of char so we can increment the occurance
            val = ord(char) - offset
            t_count[val] += 1

        # now we determine which char is added by comparing the occurances
        for i in range(len(s_count)):
            if s_count[i] != t_count[i]:
                # convert the index to char
                char = chr(i + offset)
                return char



s = 'abcd'
t = 'abcdla'
obj = Solution()
result = obj.find_the_difference(s, t)
print(result)
