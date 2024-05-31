ar = [1, 1, 2, 2, 3]

def sockMerchant(n, ar):
    # Write your code here
    pairs = 0
    count = []
    for socks in ar:
        rep = ar.count(socks)
        if rep >= 2 and socks not in count:
            pairs += rep // 2
            count.append(int(socks))
    return int(pairs)

print(sockMerchant(len(ar), ar))