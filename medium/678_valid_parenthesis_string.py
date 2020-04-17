class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        paran_stack = []
        star_stack = []

        for index, char in enumerate(s):

            print(paran_stack, star_stack)
            print("inside for loop")
            if char == "(":
                paran_stack.append(index)
            elif char == "*":
                star_stack.append(index)
            else:
                # check if stack not empty
                if paran_stack:
                    paran_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        
        while paran_stack and star_stack:
            if paran_stack[-1] > star_stack[-1]:
                return False
            else:
                paran_stack.pop()
                star_stack.pop()
        
        return len(paran_stack) == 0
            

phrase = "(*)()"
obj = Solution()
result = obj.checkValidString(phrase)
print(result)
