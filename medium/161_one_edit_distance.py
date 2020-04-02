class Solution():
    def is_one_char_away(self, s1, s2):
        """
            Takes two strings and determines whether they one or zero edits
            away. Three operations can be performed: insert a char, delete
            char and replace a char
        """
        if len(s1) == len(s2):
            print("replace a char")
            return self.replace_char(s1, s2)
        # if we can insert a char
        elif min(len(s1), len(s2)) + 1 == max(len(s1), len(s2)):
            print("insert a char")
            return self.remove_or_insert(s1, s2)
        elif min(len(s1), len(s2)) == max(len(s1), len(s2)) - 1:
            print("remove a char")
            return self.remove_or_insert(s1, s2)
        
    def replace_char(self, s1, s2):
        """
            Checks if we can replace one char and have form two same string
        """
        # if the length are not equal then we can form two same word replacing
        # one char
        
        diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1
            # if differences are more than one then we can make them same
            if diff > 1:
                return False
        
        return True

    def remove_or_insert(self, s1, s2):
        """
            Checks if we can make the two strings same by removing or inserting
            a char
            It assumes the s1 is always longer than s2
        """
        # find the longer string
        longer = s1 if len(s1) > len(s2) else s2
        shorter = s2 if len(s2) < len(s1) else s1
        print(longer, shorter)
        # find the bigger one
        index1 = 0
        index2 = 0
        diff = 0
        while index1 < len(longer) and index2 < len(shorter):
            print(longer[index1], shorter[index2])
            if longer[index1] != shorter[index2]:
                # this catches the second mismatch
                diff += 1
                print(diff)
                if diff > 1:
                    return False
                # increment the index in the longer string
                index1 += 1
            else:
                # otherwise move the indexes together
                index1 += 1
                index2 += 1
        return True


w1 = 'bale'
w2 = 'cale'
obj = Solution()
result = obj.is_one_char_away(w1, w2)
print(result)
