class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # at the beginnning set it to empty list
        combinations = []

        self.helper(digits, combinations.append, 0, [])

        return combinations

    def helper(self, digits, combinations, index, prefix=None):
        """
        Helper function to build the combination
        """
        digit_map = {
                        '1': '', '2': 'abc', '3': 'def',
                        '4': 'ghi', '5': 'jkl', '6': 'mno',
                        '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
                    }

        if prefix is None:
            prefix = []

        if len(digits) == 1:
            return digit_map[digits]
        if index >= len(digits):
            prefix.append(prefix)
            return

        pass

    def iterative_combination(self, digits):
        
        digit_map = {
                        '1': '', '2': 'abc', '3': 'def',
                        '4': 'ghi', '5': 'jkl', '6': 'mno',
                        '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
                    }
        all_combinations = [""]
        for digit in digits:
            print(f'digit: {digit}')
            current_comb = []
            print(f'curr comb {current_comb}')
            for com in all_combinations:
                for letter in digit_map[digit]:
                    print(f'com {com}, letter: {letter}')
                    current_comb.append(com + letter)
            print(f'all: {all_combinations}')
            all_combinations = current_comb
            print(f'after all: {all_combinations}')
        return all_combinations


digits = '29'
obj = Solution()
combinations = obj.iterative_combination(digits)
print(combinations)
