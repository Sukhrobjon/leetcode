class Solution(object):
    def reverse(self, n):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        negative = False

        # reverse the int
        # taking care of negative cases
        if n < 0:
            negative = True
            n = abs(n)
        # reversing the number
        while(n != 0):
            a = n % 10
            rev = rev * 10 + a
            n = n / 10
        # check if reversed number is 32 bit int
        if (-2**31) <= rev <= (2**31)-1:
            # check if the number was negative and add minus sign
            if negative:
                return (-rev)
            return rev
        else:
            return 0
