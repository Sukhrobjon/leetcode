class Solution(object):
    def shortest_palindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # we are going to use expand from middle approach
        if s == "":
            return ""
        # begging and end of the substring, we use this pointers to save up
        # so we dont have to store each valid subtring a space later,
        start = 0
        end = 0
        curr_len = 0
        longest = 0
        for i in range(len(s)):
            # this one is for odd length of palindorome
            len_1 = self.expand_from_middle(s, i, i)
            # this one is for even length of palindorome
            len_2 = self.expand_from_middle(s, i, i+1)
            # find the longer between above two
            print(f"{len_1}, {len_2}")
            curr_len = max(len_1, len_2)
            print(f"curr_len: {curr_len}, end and start {end}, {start}")
            # check if current length is greater than previous valid one
            if curr_len > end - start and curr_len > longest:
                # we need to redeclare the end and start of the substring
                start = i - ((curr_len - 1) // 2)
                end = i + (curr_len // 2)
                print(f"curr: {s[start:end+1]}")
                longest = len(s[start:end+1])
        print(f"the longest palindrome: {s[start:end+1]}")
        # if whole string is already palindrome
        if (start == 0 and end == len(s) - 1):
            return s
        # if palindrome is in the middle
        elif (start > 0 and end < len(s) - 1):
            # we need to reverse everthing from one before the start position
            reverse_sub = s[start:][::-1]
            print(f"reverse sub for middle palindrome: {reverse_sub}")
            return reverse_sub + s
        # else the longest palindrome is at the end
        elif (start > 0 and end == len(s) - 1):
            reverse_sub = s[start:][::-1]
            print(f"reverse sub for middle palindrome: {reverse_sub}")
            return reverse_sub + s

        # otherwise we need to reverse the chars after last index of substring
        # and add the reversed substring infront of the string
        reverse_sub = s[end+1:][::-1]
        print((reverse_sub))
        return reverse_sub + s

    def expand_from_middle(self, s, left, right):
        """
        Finds the length of the palindromic substring, this is helper function
        for later use to determine find the longest palindromic substring
        Args:
            s(str): original string
            left(int): left pointer
            right(int): right pointer
        Returns:
            len(int): length of the palindormic substring
        """
        # early check up
        if s is None or left > right:
            return 0

        # otherwise
        while(left >= 0 and right < len(s) and s[left] == s[right]):
            # move the pointers
            left -= 1
            right += 1
        # print(left, right)
        # length of this palidrome, -1 is to take care of boundry
        return right - left - 1


obj = Solution()
# s = "aacecaaa"
s = "abb"
result = obj.shortest_palindrome(s)
print(f"longest palindromic substring is: {result}")
