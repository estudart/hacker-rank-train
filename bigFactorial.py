def extraLongFactorials(n):
    # Write your code here
    result = int(1)
    for num in range(n):
        result = int(num+1) * int(result)
    print(result)

extraLongFactorials(4)