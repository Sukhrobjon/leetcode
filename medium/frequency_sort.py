from collections import Counter


class Solution(object):
    def frequency_sort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        s_counter = Counter(s)
        # then sort the counter
        counter_sort = sorted(s_counter.items(), key=lambda x: x[1], reverse=True)
        print(counter_sort)
        
        freq_sort = ""
        for pair in counter_sort:
            freq_sort += pair[0] * pair[1]
        
        return freq_sort

        # the other version but this was slower than the simple for loop
        # according to leetcode evaluation
        # return "".join(char[0]*char[1] for char in counter_sort)


s = ""
obj = Solution()
result = obj.frequency_sort(s)
print(result)
