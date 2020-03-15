def first_unique_char(text):
    """ 
        Given a string, find the first non-repeating character in it and
        return it's index. If it doesn't exist, return -1.
    """
    # result = 0
    ind_dict = {}
    for i in range(len(text)-1, -1, -1):
        char = text[i]
        if char not in ind_dict:
            ind_dict[char] = i
        else:
            ind_dict[char] = len(text)
        
    first_char = min(ind_dict.values())
    return first_char


text = 'loveleetcode'
result = first_unique_char(text)
print(result)
