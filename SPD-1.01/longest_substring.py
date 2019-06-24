"""
    Question: Find the longest substring of unique letters
    in a given string of n letters.
"""

# original version
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

# refactored 
def find_unique(s):
    curr = ""
    result = ""
    sd = {k:v for v, k in enumerate(s.split(''))}
    for key in sorted(sd.keys()):
        pass
