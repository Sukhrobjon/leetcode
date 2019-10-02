#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        # index is current index, starter is left pointer
        # to keep track of the start of the sub string
        index = starter = longest = 0

        while index < len(s):
            curr_char = s[index]
            # check if the char is seen before to slide back the new starter to the left
            # one after to that dubplicated char
            if curr_char in seen:
                starter = max(seen[curr_char], starter)

            cur_sub_len = index - starter + 1
            # check if current substring is greater than longest
            # and return the longer one
            longest = max(longest, cur_sub_len)

            # update the position of current char
            seen[curr_char] = index + 1

            # slide the window to right
            index += 1

        return longest


obj = Solution()
print(obj.lengthOfLongestSubstring('abcabcbb'))
