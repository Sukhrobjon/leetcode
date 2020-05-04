from collections import Counter


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        stones = Counter(S)
        count = 0
        for jewel in J:
            if jewel in stones:
                count += stones[jewel]

        return count
