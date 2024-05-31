s = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
k = 7

def make_combination(k, s):
    combination_list = []
    for number in range(len(s) - 1):
        comb = []
        for num in s:
            if s[number] == num:
                pass
            else:
                print(s[number], num)


def nonDivisibleSubset(k, s):
    # Write your code here
    valid_set = set()
    unvalid_set = set()
    for number in range(len(s)):
        for num in s:
            if s[number] == num:
                pass
            elif (s[number] + num) % k != 0:
                if s[number] not in unvalid_set and num not in unvalid_set:
                    valid_set.add(num)
                    valid_set.add(s[number])
            else:
                print('not fit')
                unvalid_set.add(num)
                unvalid_set.add(s[number])
    return len(valid_set)
        
    

print(make_combination(k, s))