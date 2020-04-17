

def compute_sum(n, total):
    """
        Compute the total sum range 0 to n
    """
    # print(n)
    # base case, if you reach n is 0 then you want to return it
    print(total[0])
    if n == 0:
        return 0
    total[0] = total[0] + compute_sum(n-1, total)
    # else the previous value + (n - 1)
    # return n + compute_sum(n-1)

n = 5  # expected 15
total = [0]
print(compute_sum(3, total))
