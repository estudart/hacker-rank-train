s = [2, 2, 1, 3, 2]
d = 4
m = 2


def birthday(s, d, m):
    count = 0
    for i in range(len(s) - m + 1):
        if sum(s[i:i+m]) == d:
            count+=1
    return count


print(birthday(s, d, m))