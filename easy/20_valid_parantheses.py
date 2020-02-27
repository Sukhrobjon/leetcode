"""
Description: Given a string containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
NOTE: An empty string is also considered valid.

"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 != 0:
            return False

        dict_paren = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for char in s:
            # check if the char is opening parentheses
            if char in dict_paren:
                # add the closing pair
                val = dict_paren[char]
                stack.append(val)

            else:
                if char != stack.pop():
                    return False

        return len(stack) == 0


s = ''
obj = Solution()
result = obj.isValid(s)
print(result)
