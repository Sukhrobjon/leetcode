class Solution:
    def countElements(self, arr):
        # create hashtable
        all_numbers = {}

        for num in arr:
            all_numbers[num] = "val"
        count = 0
        
        for num in arr:
            if num + 1 in all_numbers:
                count += 1

        return count