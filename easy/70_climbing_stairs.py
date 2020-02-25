'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways
can you climb to the top?

Note: Given n will be a positive integer.
'''


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.helper(n)

    def helper(self, n, memo=None):
        if memo is None:
            memo = {}

        if n == 0 or n == 1:
            return 1
        # if result at the ith index is not computed
        # compute it and assign the value
        if n not in memo:
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)

        return memo[n]
