# Complete the 'missingCharacters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

s = '8hypotheticall024y6wxz'

def missingCharacters(s):
    # Write your code here
    
    string_list = []
    int_list = []
    
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z']
    
    for char in s:
        if str(char) in letters:
            string_list.append(char)
        elif int(char) in numbers:
            int_list.append(int(char))
    
    for letter in string_list:
        if letter in letters:
            try:
                letters.remove(letter)
            except ValueError:
                print("letter already removed")
    
    for num in int_list:
        if num in numbers:
            try:
                numbers.remove(num)
            except Exception:
                print("number already removed")
    
    return str("".join(str(number) for number in numbers)) + str("".join(letters))

print(missingCharacters(s))