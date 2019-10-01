"""
Write a function that reverses a string. The input string is given as an array
of characters char[].

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
"""


class Solution(object):
    def reverse_string(self, s):
        """
        Reserse the string
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        front = 0
        back = len(s) - 1
        while front < back:
            s[front], s[back] = s[back], s[front]
            front += 1
            back -= 1
        return s

obj = Solution()
word = ["H", "a", "n", "n", "a"]
result = obj.reverse_string(word)
print(result)
