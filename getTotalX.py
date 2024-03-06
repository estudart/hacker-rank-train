a = [2, 4]
b = [16, 32, 96]


def getTotalX(a, b):
    # Write your code here
    maxi_a = max(a)
    mini_b = min(b)
    number_factor = []

    number = maxi_a
    # begin to check all numbers between max(b) and min(b)
    while number <= mini_b:
        count = 0
        for factor in a:
            if number % factor != 0:
                pass
            else:
                count += 1

            if count == len(a):
                count = 0
                for divi in b:
                    if divi % number != 0:
                        pass
                    else:
                        count += 1

                    if count == len(b):
                        number_factor.append(number)
        number += 1
    return len(number_factor)

print(getTotalX(a, b))