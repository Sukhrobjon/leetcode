class Solution:
    def calculate(self, s: str):
        # to hold the numbers
        stack = []
        sign = '+'
        num = 0
        # operators = {'+': 0, '-': 0, '*': 1, '/': 1}
        for i in range(len(s)):
            # check if current char is digit
            char = s[i]
            if char.isdigit():
                num = num * 10 + int(char)
        
            # check for operator
            if i + 1 == len(s) or (char == '+' or char == '-' or char == '*' or char == '/'):
                if sign == '+':
                    # we store for later
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    # this is like poping the last element
                    # and perform whatever the number at the top of stack
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    print("devide", stack)
                    stack[-1] = int(stack[-1] / float(num))
                # reset the values for sign and number
                sign = char
                num = 0
        
        return (stack)


s = " 3/2 "
obj = Solution()
result = obj.calculate(s)
print(result)
