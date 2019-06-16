def optimized_longest_substring(word):
    seen = {}
    # index is current index, starter is left pointer
    # to keep track of the start of the sub string
    index = starter = longest = 0

    while index < len(word):
        curr_char = word[index]
        # check if the char is seen before to slide back the new starter to the left
        # one after to that dubplicated char
        if curr_char in seen:
            starter = max(seen[curr_char], starter)

        cur_sub_len = index - starter + 1
        # check if current substring is greater than longest
        # and return the longer one
        longest = max(longest, cur_sub_len)

        # update the position of current char
        seen[curr_char] = index + 1

        # slide the window to right
        index += 1

    return longest


a = 'abcabcbb'
b = 'dvdf'
c = 'pwwkew'
print(optimized_longest_substring(b))
