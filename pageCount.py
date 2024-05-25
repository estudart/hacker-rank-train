import math
n = 10 # number of pages on the book
p = 9 # number of the page to go to

def pageCount(n, p):
    # Write your code here
    turns_from_start = (p - 1) / 2
    if n - p == 1 and n % 2 == 0:
        turns_from_end = 1
    else:
        turns_from_end = (n - p) / 2
    print(turns_from_end, turns_from_start)
    return int(min(math.ceil(turns_from_start), math.floor(turns_from_end)))


print(pageCount(n=n, p=p))