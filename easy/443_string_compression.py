class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        from collections import Counter
        counter = Counter(chars)
        items = []
        for k, v in counter.items():
            items.append(k)
            if v > 1:
                items.append(v)
        print(items)
        # naive solution
        count = 1
        com_str = []
        for i in range(len(chars) - 1):
            char = chars[i]
            print(char)
            if chars[i] == chars[i+1]:
                count += 1
            else:
                # we see the first unmatch
                com_str.append(char)
                print(count)
                if count > 1:
                    com_str.append(count)
                # reset the count for new char
                count = 1
        
        return com_str

obj = Solution()
chars = ["a", "a", "b", "b", "c", "c", "c"]
result = obj.compress(chars)
print(result)
