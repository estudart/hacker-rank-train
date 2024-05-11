k = 3
ar = [1, 3, 2, 6, 1, 2]
n = 6

def divisibleSumPairs(n, k, ar):
    div_list = []
    for index in range(n):
        num = 1
        dif = len(ar) - index
        while dif != 0:
            try:
                n1 = ar[index]
                n2 = ar[index + num]
                if (n1 + n2) % k == 0:
                    div_list.append((index + 1, index + num + 1))  
            except:
                print(div_list)
            dif-=1
            num+=1

divisibleSumPairs(n, k, ar)