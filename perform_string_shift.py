class Solution(object):

    def string_shift_optimized(self, s, shift):
        """
            Optimizing the number of shifting by canceling
            left and right shifts and perform the rotation once
        """
        rotation = 0
        for direction, move in shift:
            # print(direction, move)
            if direction == 0:
                rotation += move
            else:
                rotation -= move
        # print(move)
        # to take care of negative val
        rotation = rotation % len(s)
        print(rotation)
        # we can just do the left rotation
        return s[rotation:] + s[:rotation]

    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        s = list(s)
        for pair in shift:
            side = pair[0]
            number_rotation = pair[1]
            # do left rotation
            if side == 0:
                s = self.left_rotation(s, number_rotation)

            else:
                s = self.right_rotation(s, number_rotation)
            print(f"after each stage {side} and string {s}")
        
        return "".join(s)

    def left_rotation(self, s, number_rotation):
        """
            rotate the string to left side by given number of times
        """
        if number_rotation >= len(s):
            number_rotation = number_rotation % len(s)
        
        s[:] = s[number_rotation:] + s[:number_rotation]

        return s

    def right_rotation(self, s, number_rotation):
        """
            rotate the string to left side by given number of times
        """
        if number_rotation >= len(s):
            number_rotation = number_rotation % len(s)
        # s[-k:] last k items in the array
        # s[:-k] everything but not last k items
        s[:] = s[-number_rotation:] + s[:-number_rotation]

        return s


word = "abcdefg"
shift = [[1, 1], [1, 1], [0, 2], [1, 3]]
obj = Solution()
result = obj.string_shift_optimized(word, shift)
print(result)  # efgabcd
