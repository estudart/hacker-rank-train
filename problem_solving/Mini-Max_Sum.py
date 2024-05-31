arr = [1, 1, 5, 7, 7]

def miniMaxSum(arr):
    mini = min(arr)
    mini_soma = 0
    mini_repeat = 0
    maxi = max(arr)
    maxi_soma = 0
    maxi_repeat = 0
    # print(mini, maxi)
    for num in arr:
        if num == maxi:
            maxi_repeat += 1
        if num == mini:
            mini_repeat += 1
    for num in arr:
        if num != maxi:
            mini_soma += num
        elif num == maxi and maxi_repeat > 1:
            mini_soma += num
            maxi_repeat -= 1
    for num in arr:
        if num != mini:
            maxi_soma += num
        elif num == mini and mini_repeat > 1:
            maxi_soma += num
            mini_repeat -= 1
    print(mini_soma, maxi_soma)




miniMaxSum(arr)