"""Problem 2: Given an array of integers, replace each element 
of the array with product of every other element in the array 
without using the division operator.
Example input 1: 
[1, 2, 3, 4, 5] = > should return output: [120, 60, 40, 30, 24]

Example input 2: 
[5, 3, 4, 2, 6, 8] = >  should return output: [1152, 1920, 1440, 2880, 960, 720]
"""

# slicing the array arr[0:self-1]+arr[self:]
# start two pointers at the current num we want to ignore and expand the pointer to the sides


def product_no_self(numbers):
    start = 0
    end = 0
    index = 0
    pro = 1
    output = []
    # bound check
    while index < len(numbers):     # [1, 2, 3, 4, 5] O(n)
        curr = numbers[index]
        start = index - 1  # 2, 1
        end = index + 1   # 4, 5
        pro = 1
        while start > -1 or end < len(numbers): # O(n)
            
            if start > -1:
                pro *= numbers[start]
                start -= 1
            if end < len(numbers):
                pro *= numbers[end]
                end += 1
        output.append(pro)
        index += 1
    return output


numbers = [1, 2, 3, 4, 5]
# space is O(n)
# run time is O(n^2)
print(product_no_self(numbers))
