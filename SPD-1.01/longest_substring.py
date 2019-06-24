"""
    Question: Find the longest substring of unique letters
    in a given string of n letters.
"""

def findUnique(s):
    curr = ""
    result = ""
    sd = enum(s.split(""))
    for key in sorted(sd.keys()):
        if char not in curr:
            curr += sd[key]
            if len(curr) > len(result):
                result = curr
        else:
            index += 1
